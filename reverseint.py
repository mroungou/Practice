# Exercise 14: Reverse a given integer number

# Given:

# 76542

# Expected output:

# 24567
num = 76524
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num *= 10
    reversed_num += digit
    num //= 10
print(reversed_num)
