# Exercise 6: Count the total number of digits in a number

# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.

number = 75869
digit_counter = 0
while number != 0:
    number //= 10
    digit_counter += 1
print(digit_counter)
