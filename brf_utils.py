def duplicate(stack):
    stack.append(stack[-1])

def swap(stack):
    stack[-2], stack[-1] = stack[-1], stack[-2]

def inc(stack):
    stack[-1] += 1

def dec(stack):
    stack[-1] -= 1

def print_string(stack):
    print(stack.pop(), end="")

def print_char(stack):
    print(chr(stack.pop()), end="")

def add(stack):
    stack.append(stack.pop() + stack.pop())

def sub(stack):
    stack.append(stack.pop() - stack.pop())

def mul(stack):
    stack.append(stack.pop() * stack.pop())

def div(stack):
    stack.append(stack.pop() / stack.pop())

def mod(stack):
    stack.append(stack.pop() % stack.pop())

def floor_div(stack):
    stack.append(stack.pop() // stack.pop())

def less(stack):
    stack.append(int(stack.pop() < stack.pop()))

def equals(stack):
    stack.append(int(stack.pop() == stack.pop()))

def greater(stack):
    stack.append(int(stack.pop() > stack.pop()))
