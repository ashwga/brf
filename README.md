# Todo:
- [ ] file inclusion
- [ ] special characters (like \n)

# Symbols (aka instructions)
## def (define variable/symbol)
Usage:
`"NAME" [ CODE ] def`
Example:
`"pi" [ 3.1415 ] def # will add a symbol called pi`

## dup (duplicate value on stack):
Example:
`"string" dup`

## swp (swap two values on stack):
Example:
`"string 1" "string 2" swp prt prt # will print string 1 then string 2`

## prt (pop and print value from stack):
Example:
`"Hello, world!" prt # will print Hello, world!`

## prc (pop int from stack and print it as an ascii character):
Example:
`65 prc # will print A`

-----
# Math
## Addition:
- Regular:
    - Example: `1 2 + prt # will print 3`
- Increment:
    - Example: `1 ++ prt # will print 2`

## Subtraction:
- Regular:
    - Example: `10 7 - prt # will print 3`
- Increment:
    - Example: `1 -- prt # will print 0`

## Multiplication:
- Regular:
    - Example: `2 3 * prt # will print 6`

## Division:
- Regular:
    - Example: `5 2 / + prt # will print 2.5`
- Modulo:
    - Example: `3 2 % prt # will print 1`
- Floor division:
    - Example: `10 3 // prt # will print 3`

## Comparing two values:
- Less than:
    - Example: `10 2 < prt # will print 0`
    - Example: `1 2 < prt # will print 1`
- Greater than:
    - Example: `10 2 > prt # will print 1`
    - Example: `1 2 > prt # will print 0`
- Equal:
    - Example: `1 1 = prt # will print 1`
    - Example: `0 1 = prt # will print 0`

# Notes:
### **For some reason the last character of code isn't read, remember to add spaces at the end of code blocks and files**
