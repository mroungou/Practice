# Exercise 3: Calculate the sum of all numbers from 1 to a given number

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Expected Output:

# Enter number 10
# Sum is:  55

num = int(input("Enter a number: "))
total = 0


for i in range(num+1):
    total += i
print(f"Sum is: {total}")

# could also be done using the built-in sum() function

summation = sum(range(1, num + 1))
print(summation)
