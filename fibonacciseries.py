# Exercise 12: Display Fibonacci series up to 10 terms


# The Fibonacci Sequence is a series of numbers. The next number is found by adding
# up the two numbers before it. The first two numbers are 0 and 1.

# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

# Expected output:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
num1 = 0
num2 = 1
result = num1 + num2
counter = 2  # counter set intially to 2 because we want the first 10 numbers. 1 and 0 are given in the beginning
print("Fibonacci sequence: ")
print(num1, num2, end=' ')
while counter != 10:
    print(result, end=" ")
    # updating the values
    num1 = num2
    num2 = result
    result = num1 + num2
    counter += 1
