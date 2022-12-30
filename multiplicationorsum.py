# Exercise 1: Calculate the multiplication and sum of two numbers

# Given two integer numbers return their product only if
# the product is equal to or lower than 1000, else return their sum.

def multiplication(number1, number2):
    product = number1 * number2
    sum = number1 + number2
    if number1 * number2 <= 1000:
        return product
    else:
        return sum


n1 = 30
n2 = 40

print(multiplication(n1, n2))
