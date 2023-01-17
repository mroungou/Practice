# Exercise 18: Print the following pattern

# Write a program to print the following start pattern using the for loop

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(6):
    if i <= 5:
        print('* ' * i)
    if i == 5:
        for i in range(4, 0, -1):
            print('* '*i)

# another option
rows = 5
for i in range(0, rows):
    for j in range(0, i+1):
        print('*', end=' ')
    print("\r")
for i in range(rows, 0, -1):
    for j in range(0, i-1):
        print('*', end=' ')
    print("\r")
