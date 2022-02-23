# Todo (in order of priority):
- 0.0.3:
    - [ ] reading files
    - [ ] arguments (argv, argc?)
    - [ ] syscalls?
    - [x] actual variables
- 0.0.2:
    - [x] special characters (like \n)
    - [x] input
    - [x] while loops
    - [x] file inclusion
    - [x] if statements
    - [x] comments

# Symbols (aka instructions)
## def (define symbol)
Usage:
`"NAME" [ CODE ] def`
Example:
`"pi" [ 3.1415 ] def # will add a symbol called pi`

## assign (define variable)
Usage:
`"NAME" value assign`

## read (read variable and put on stack)
Usage:
`"NAME" read`

## dup (duplicate value on stack)
Example:
`"string" dup`

## swp (swap two values on stack)
Example:
`"string 1" "string 2" swp prt prt # will print string 1 then string 2`

## rot (rotate 3 values on stack)
Example:
`1 2 3 rot prt prt prt # will print 231`

## prt (pop and print value from stack)
Example:
`"Hello, world!" prt # will print Hello, world!`

## prc (pop int from stack and print it as an ascii character)
Example:
`65 prc # will print A`

## drop (drop top value from stack)
Example:
`2 1 drop prt # will print 2`

## dropall (empties the stack)
Example:
`2 1 drop prt # will throw an error`

## in_s (input string)
Example:
`in_s <user inputs abc> prt # will print abc`

## in_c (input character (cuts off everything after first character))
Example:
`in_c <user inputs abc> prt # will print a`

## split (split string by character(s))
Usage:
`string split_char split`
Notes:
If split_char is empty it'll output every character in string by itself
`"abcde" "" split prt prt prt prt prt # will print edcba`

## here (replaced by its location)
Example:
`here prt # will print tmp.brf:1:1 if saved in tmp.brf`

## i2a (int to ascii)
Example:
`65 i2a 66 i2a + prt # will print AB`

## a2i (ascii to int)
Example:
`"A" a2i prt # will print 65`

## if (if statement)
Usage:
`val_to_check [ if true ] if`
Notes:
**Warning: Consumes val_to_check**
Examples:
`1 [ "yes" prt ] if # will print yes`
`0 [ "yes" prt ] if # will not print anything`

## if_else (if_else statement)
Usage:
`val_to_check [ if true ] [ if false ] if_else`
Notes:
**Warning: Consumes val_to_check**
Examples:
`1 [ "yes" prt ] [ "no" prt ] if # will print yes`
`0 [ "yes" prt ] [ "no" prt ] if # will print no`

## while (while loop)
Usage:
`val [ code_to_exec ] while # will execute code_to_exec if val is truthy and continue to execute it while the top value is truthy`
Notes:
Consumes top value to check if truthy

## do_while (do while loop)
Usage:
`[ code to exec ] do_while # will execute code_to_exec once and then do regular while loop`

## /include (include a file)
Usage:
`/include FILENAME`
Notes:
Adds code from FILENAME to current file
**Warning: /include loops can occur**

-----
# Math
## Addition:
- Regular:
    - Example: `1 2 + prt # will print 3`
    - Notes: can be used for concatenating strings
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

## Bitwise operations:
- not:
    - Example: `1 not prt # will print 0`
- and
    - Example: `2 3 and prt # will print 2`
- or
    - Example: `4 3 or prt # will print 7`
- xor
    - Example: `7 7 xor prt # will print 0`

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
