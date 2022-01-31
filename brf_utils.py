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

def in_s(stack):
    stack.append(input())

def in_c(stack):
    stack.append(input()[0])

def i2a(stack):
    stack.append(chr(stack.pop()))

def a2i(stack):
    stack.append(ord(stack.pop()))

def drop(stack):
    stack.pop()

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
