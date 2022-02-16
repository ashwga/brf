import brf

symbols = {}
variables = {}
stack = []

print("Input empty line for stack; /reset to reset symbols and variables")

try:
    while 1:
        try:
            user_input = input("\n> ") + " "
            if user_input.strip() == "/reset":
                symbols = {}
                variables = {}
                print("Symbols and variables cleared.")
                continue
            elif user_input.strip() == "/clear":
                stack = []
                print("Stack cleared.")
                continue
            elif user_input.strip() == "/exit":
                exit(0)
            try:
                if user_input.strip() != "":
                    tokens = brf.preprocess(user_input)
                    brf.exec_tokens(tokens, stack, symbols, variables, False, "stdin")
                else:
                    print(f"{', '.join(str(i) for i in stack)}")
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")

except EOFError as e:
    print("bye!")
