# Exercise 8: Print the following pattern

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    print(f'{i} '*i)

# Another option is to use a nested loop which I'll try next

# outer loop
for i in range(1, 6):
    # inner loop
    for j in range(i):
        print(i, end=' ')
    print('')

# the outer loop represents the number of rows, i.e. how many times the program will run
# the inner loop represents the columns, and it'll run dependent on which iteration the outer loop is on
# e.g. when i = 2 the inner loop will run twice before it is done and returns to the outer loop
# that is the reason 2 is printed twice and so on
