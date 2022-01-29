import brf

symbols = {}
stack = []

print("Input empty line for stack")

try:
    while 1:
        user_input = input("\n> ") + " "
        if user_input.strip() != "":
            tokens = brf.preprocess(user_input)
            brf.exec_tokens(tokens, stack, symbols, False)
        else:
            print(f"{', '.join(str(i) for i in stack)}")

except (KeyboardInterrupt, EOFError):
    print("bye!")
    exit(0)
