import sys
import argparse
import brf_utils as bu

VERSION = "0.0.1"

std_symbols = {
    "def": None, # implemented here
    "dup": bu.duplicate,
    "swp": bu.swap,
    "prt": bu.print_string,
    "prc": bu.print_char,
    "if":  None, # implemented here
    "+":   bu.add,
    "++":  bu.inc,
    "-":   bu.sub,
    "--":  bu.dec,
    "*":   bu.mul,
    "/":   bu.div,
    "%":   bu.mod,
    "//":  bu.floor_div,
    "<":   bu.less,
    "=":   bu.equals,
    ">":   bu.greater
}

def isnum(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def exec_brf_code(s, stack, symbols, verbose):
    global std_symbols
    if isnum(s) or "[" in s or "\"" in s:
        stack.append(s if isnum(s) else s.strip("[]\""))
    elif s == "def":
        symbols[stack.pop().strip("\"")] = stack.pop().strip("\"")
    elif s == "if":
        f_code = stack.pop()
        t_code = stack.pop()
        v = stack.pop()
        if v:
            exec_tokens(preprocess(t_code), stack, symbols, verbose)
        else:
            exec_tokens(preprocess(f_code), stack, symbols, verbose)
    elif s in std_symbols:
        std_symbols[s](stack)
    elif s in symbols:
        exec_tokens(preprocess(symbols[s]), stack, symbols, verbose)

def preprocess(code):
    tokens = []
    token_str = ""

    clevel = 0
    is_inside_str = False
    comment = False

    for idx, i in enumerate(code):
        if i == "#":
            comment = True
        elif i == "\n":
            comment = False

        if comment:
            continue

        if (i == " " or i == "\n" or idx == len(code) - 1) and (clevel == 0 and not is_inside_str):
            if token_str == "/include":
                filename = code[idx:idx+code[idx:].find("\n")].strip(" \n")
                with open(filename, "r") as f:
                    data = f.read()
                tokens.extend(preprocess(data))
                comment = True # workaround
            else:
                tokens.append(token_str)
            token_str = ""
        else:
            token_str += i
            if i == "[":
                clevel += 1
            elif i == "]":
                clevel -= 1
            elif i == "\"" and ((code[idx-1] != "\\" and idx - 1 >= 0) or (idx == 0)):
                is_inside_str = not is_inside_str

    if clevel != 0:
        if clevel > 0:
            print("no matching \"]\" found")
        else:
            print("no matching \"[\" found")
        exit(1)

    if is_inside_str:
        print("unmatched \" found")
        exit(1)

    tokens = list(map(lambda x: x if isinstance(x, (int, float)) else (int(x) if x.isdigit() else (float(x) if isnum(x) else x)), tokens))
    tokens = [x for x in tokens if x != ""]

    return tokens

def exec_tokens(tokens, stack, symbols, verbose):
    global std_symbols
    for i in tokens:
        if verbose:
            print(f"{stack = } {i = } ({type(i).__name__})")
        if not isnum(i):
            if (i not in std_symbols and i not in symbols) and "\"" not in i and "[" not in i:
                print(f"ERROR: undefined symbol \"{i}\"")
                break
        exec_brf_code(i, stack, symbols, verbose)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"Python interpreter for brf, an esolang, v{VERSION}")
    parser.add_argument("filename", metavar="FILE", nargs="?", help="File to run, omit or - for stdin")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_const", const=True, default=False, help="Print additional info")
    args = parser.parse_args()

    # prepare for execution
    code = ""

    if args.filename in [None, "-"]:
        code = sys.stdin.read()
    else:
        with open(args.filename, "r") as f:
            code = f.read()

    tokens = preprocess(code)

    symbols = {}
    stack = []

    # execute
    exec_tokens(tokens, stack, symbols, args.verbose)
