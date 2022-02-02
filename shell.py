import brf

symbols = {}
stack = []

print("Input empty line for stack")

try:
    while 1:
        user_input = input("\n> ") + " "
        try:
            if user_input.strip() != "":
                tokens = brf.preprocess(user_input)
                brf.exec_tokens(tokens, stack, symbols, False, "stdin")
            else:
                print(f"{', '.join(str(i) for i in stack)}")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")

except (KeyboardInterrupt, EOFError) as e:
    if isinstance(e, EOFError):
        print("bye!")
        exit(0)
