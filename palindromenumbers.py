# Exercise 9: Check Palindrome Number

# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is same after reverse.
# For example 545, is the palindrome numbers


number = int(input('Enter a number: '))  # the number you want to reverse
num_reverse = 0

while number != 0:
    # taking the modulo will give you the last digit of the number
    current_digit = number % 10
    # to add the digit, multiply the current reversed number by 10 and add the current digit
    num_reverse = 10*num_reverse
    num_reverse += current_digit
    number //= 10  # to remove the last number from the number divide it by 10

print(f'Reversed Number is: {num_reverse}')
