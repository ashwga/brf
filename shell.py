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
                brf.exec_tokens(tokens, stack, symbols, False)
            else:
                print(f"{', '.join(str(i) for i in stack)}")
        except (KeyboardInterrupt, IndexError) as e:
            if e == IndexError:
                print("ERROR: pop from empty stack")
            elif e == KeyboardInterrupt:
                print("KeyboardInterrupt")

except (KeyboardInterrupt, EOFError):
    print("bye!")
    exit(0)
