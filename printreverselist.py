# Exercise 8: Print list in reverse order using a loop

# Given:

list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10

length = len(list1)
counter = -1
while counter >= -length:
    print(list1[counter])
    counter -= 1

# using reversed()
new_list = reversed(list1)
for i in new_list:
    print(i)

# option 3
for i in range(length - 1, -1, -1):
    print(list1[i])
