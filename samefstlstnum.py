# # Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

def checklastfirst(something):
    print('Given number list:', something)
    first = something[0]
    last = something[-1]
    if first == last:
        return True
    else:
        return False


numbers = [1, 3, 6, 8, 9, 1]
print('the resuls is:', checklastfirst(numbers))


numbers = [1, 3, 6, 8, 9, 10]
print('the resuls is:', checklastfirst(numbers))
