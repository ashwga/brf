def isnum(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def duplicate(stack):
    stack.append(stack[-1])

def swap(stack):
    stack[-2], stack[-1] = stack[-1], stack[-2]

def rot(stack):
    c = stack.pop()
    b = stack.pop()
    a = stack.pop()
    stack.extend((a, c, b))

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

def split(stack):
    b, a = stack.pop(), stack.pop()
    if b != "":
        for i in a.split(b):
            stack.append(i)
    else:
        for i in a:
            stack.append(i)

def i2a(stack):
    stack.append(chr(stack.pop()))

def n2s(stack):
    stack.append(str(stack.pop()))

def s2n(stack):
    v = stack.pop()
    v = int(v) if v.isdigit() else float(v)
    stack.append(v)

def s2f(stack):
    v = stack.pop()
    v = float(v)
    stack.append(v)

def s2i(stack):
    v = stack.pop()
    v = int(float(v))
    stack.append(v)

def a2i(stack):
    stack.append(ord(stack.pop()))

def drop(stack):
    stack.pop()

def dropall(stack):
    while stack:
        stack.pop()

def add(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b + a)

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

def bit_not(stack):
    stack.append(0 if stack.pop() else 1)

def bit_and(stack):
    stack.append(stack.pop() & stack.pop())

def bit_or(stack):
    stack.append(stack.pop() | stack.pop())

def bit_xor(stack):
    stack.append(stack.pop() ^ stack.pop())

def less(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(int(a < b))

def equals(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(int(a == b))

def greater(stack):
    b, a = stack.pop(), stack.pop()
    stack.append(int(a > b))
