# Exercise 13: Find the factorial of a given number

# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:


# 120
num = int(input('Type a number: '))
result = 1
print(f'{num}!')
while num != 0:
    result *= num
    num -= 1
print(f"The result is: {result}")
