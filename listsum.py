# Create a new list from a two list using the following condition

# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
# Expected Output:

# result list: [25, 35, 40, 60, 90]


def combinelist(*lists):
    newlist = []
    for num in lists[0]:
        if num % 2 == 0:
            newlist.append(num)

    for num in lists[1]:
        if num % 2 != 0:
            newlist.append(num)
    # print(newlist)
    return newlist


print(combinelist([10, 40, 15], [33, 47, 89]))
