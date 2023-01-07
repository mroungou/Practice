# Exercise 15: Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp.

# Note here exp is a non-negative integer, and the base is an integer.
# expected output
# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result *= base
        num -= 1
    print(f"{base} to the power of {exp} is {result}")


exponent(2, 3)
