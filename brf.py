import sys
import argparse
import brf_utils as bu

VERSION = "0.0.2"

std_symbols = {
    "def":      None, # implemented here
    "assign":   None, # implemented here
    "read":     None, # implemented here
    "dup":      bu.duplicate,
    "swp":      bu.swap,
    "rot":      bu.rot,
    "prt":      bu.print_string,
    "prc":      bu.print_char,
    "in_s":     bu.in_s,
    "in_c":     bu.in_c,
    "split":    bu.split,
    "i2a":      bu.i2a,
    "a2i":      bu.a2i,
    "n2s":      bu.n2s,
    "s2n":      bu.s2n,
    "s2f":      bu.s2f,
    "s2i":      bu.s2i,
    "drop":     bu.drop,
    "dropall":  bu.dropall,
    "if":       None, # implemented here
    "while":    None, # implemented here
    "do_while": None, # implemented here
    "+":        bu.add,
    "++":       bu.inc,
    "-":        bu.sub,
    "--":       bu.dec,
    "*":        bu.mul,
    "/":        bu.div,
    "%":        bu.mod,
    "//":       bu.floor_div,
    "not":      bu.bit_not,
    "and":      bu.bit_and,
    "or":       bu.bit_or,
    "xor":      bu.bit_xor,
    "<":        bu.less,
    "=":        bu.equals,
    ">":        bu.greater
}

def exec_brf_code(s, stack, symbols, variables, verbose, fn):
    global std_symbols
    if bu.isnum(s) or "[" in s or "\"" in s:
        stack.append(s if bu.isnum(s) else s.strip("[]\""))
    elif s == "def":
        symbols[stack.pop().strip("\"")] = stack.pop().strip("\"")
    elif s == "assign":
        variables[stack.pop().strip("\"")] = stack.pop()
    elif s == "read":
        stack.append(variables[stack.pop()])
    elif s == "if":
        f_code = stack.pop()
        t_code = stack.pop()
        v = stack.pop()
        if v:
            exec_tokens(preprocess(t_code), stack, symbols, variables, verbose, fn)
        else:
            exec_tokens(preprocess(f_code), stack, symbols, variables, verbose, fn)
    elif s == "while":
        code_tokens = preprocess(stack.pop())
        v = stack.pop()
        while v:
            exec_tokens(code_tokens, stack, symbols, variables, verbose, fn)
            v = stack.pop()
    elif s == "do_while":
        code = stack.pop()
        v = True
        while v:
            exec_tokens(preprocess(code), stack, symbols, variables, verbose, fn)
            v = stack.pop()
    elif s in std_symbols:
        std_symbols[s](stack)
    elif s in symbols:
        exec_tokens(preprocess(symbols[s]), stack, symbols, variables, verbose, fn)

def preprocess(code):
    tokens = []
    token_str = ""

    clevel = 0
    is_inside_str = False
    comment = False

    line_count = 1
    col_count = 1

    for idx, i in enumerate(code):
        if i == "\n":
            line_count += 1
            col_count = 1
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
                # kind of safe fix for escaped escaped special characters still being replaced
                token_str = token_str.replace("\\\\n", str(hash(token_str))).replace("\\n", "\n").replace(str(hash(token_str)), "\\n")
                token_str = token_str.replace("\\\\r", str(hash(token_str))).replace("\\r", "\r").replace(str(hash(token_str)), "\\r")
                token_str = token_str.replace("\\\\t", str(hash(token_str))).replace("\\t", "\t").replace(str(hash(token_str)), "\\t")
                tokens.append([token_str, (line_count, col_count)])
            token_str = ""
        else:
            col_count -= 1 # just so col_count points to the start of the symbol
            token_str += i
            if i == "\"" and ((code[idx-1] != "\\" and idx - 1 >= 0) or (idx == 0)):
                is_inside_str = not is_inside_str
            if not is_inside_str:
                if i == "[":
                    clevel += 1
                elif i == "]":
                    clevel -= 1
        col_count += 1

    if clevel != 0:
        if clevel > 0:
            print("no matching \"]\" found")
        else:
            print("no matching \"[\" found")
        exit(1)

    if is_inside_str:
        print("unmatched \" found")
        exit(1)

    tokens = [i for i in tokens if i[0] != ""]

    for idx, i in enumerate(tokens):
        if i[0].isdigit():
            tokens[idx][0] = int(i[0])
        elif bu.isnum(i[0]):
            tokens[idx][0] = float(i[0])


    return tokens

def exec_tokens(tokens, stack, symbols, variables, verbose, fn):
    global std_symbols
    for i in tokens:
        if verbose:
            print(f"{stack = } {i = } ({type(i[0]).__name__})")
        if not bu.isnum(i[0]):
            if (i[0] not in std_symbols and i[0] not in symbols and i[0] not in variables) and "\"" not in i[0] and "[" not in i[0]:
                print(f"\n{fn}:{i[1][0]}:{i[1][1]}: ERROR: undefined symbol \"{i[0]}\"")
                break
        try:
            exec_brf_code(i[0], stack, symbols, variables, verbose, fn)
        except (IndexError, KeyError) as e:
            if isinstance(e, IndexError):
                print(f"\n{fn}:{i[1][0]}:{i[1][1]}: ERROR: Cannot pop from empty stack")
            if isinstance(e, KeyError):
                print(f"\n{fn}:{i[1][0]}:{i[1][1]}: ERROR: Undefined variable")
            if fn != "stdin":
                exit(1)

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
    variables = {}
    stack = []

    # execute
    exec_tokens(tokens, stack, symbols, variables, args.verbose, args.filename)
