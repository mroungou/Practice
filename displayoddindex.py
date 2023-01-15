# # Exercise 15: Use a loop to display elements from a given list present at odd index positions

# # Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output:

# 20 40 60 80 100

for i in range(len(my_list)):
    # checks whether the index is an odd number or not
    if i % 2 != 0:
        print(my_list[i], end=" ")

# another option
# start from index 1 and with step 2(1,3,5,7etc)
for i in my_list[1::2]:
    print(i, end=' ')

# using enumerate
for index, ele in enumerate(my_list):
    if index % 2 != 0:
        print(ele, end=" ")
