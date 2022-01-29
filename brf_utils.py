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
    a, b = stack.pop(), stack.pop()
    stack.append(b - a)

def mul(stack):
    stack.append(stack.pop() * stack.pop())

def div(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(a / b)

def mod(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(a % b)

def floor_div(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(a // b)

def less(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(int(a < b))

def equals(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(int(a == b))

def greater(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(int(a > b))
