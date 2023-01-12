# Exercise 11: Write a program to display all prime numbers within a range


# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a
# natural number greater than 1 that is not a product of two smaller natural numbers

# Examples:

# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.

for numbers in range(25, 50):
    #    prime numbers are greater than 1
    # if prime number is less than or equal to one it is not  a prime number
    if numbers > 1:
        for i in range(2, numbers):
            if (numbers % i) == 0:
                # not a prime number
                # stop inner loop and look at the next number
                break
        else:
            print(numbers)
