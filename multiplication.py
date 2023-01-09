# Exercise 4: Write a program to print multiplication table of a given number

# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

num = int(input("Enter a number: "))
for i in range(1, 11):
    multiple = num * i
    print(multiple)
