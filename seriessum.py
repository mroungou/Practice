# Exercise 17: Find the sum of the series upto n terms

# Write a program to calculate the sum of series up to n term. For example,
#  if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:

# # number of terms
# n = 5
# Expected output:


# 24690
num_iterations = 5
num = 2
total = 0

for i in range(0, num_iterations):
    print(num, end='+')
    total += num
    # calculate the next term
    num = num * 10+2
print(f'Sum of series is {total}')
