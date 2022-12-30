# Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

current_number = None
previous_number = None
total = 0

for i in range(10):
    if (current_number and previous_number) is None:
        current_number = 0
        previous_number = 0
        total = 0
        print(
            f'Current Number {current_number} Previous Number {previous_number} Sum: {total}')
        current_number += 1
        total = previous_number + current_number
    elif (current_number and previous_number) is not None:
        print(
            f'Current Number {current_number} Previous Number {previous_number} Sum: {total}')
        current_number += 1
        previous_number += 1
        total = previous_number + current_number
