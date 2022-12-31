# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting
# from zero up to n and return a new string.

# For example:

# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.


string = input('ENTER WORD: ')
slice_index = int(input("Enter cutting point: "))
while True:
    if slice_index > len(string):
        print('Slice Index cannot be larger than length of string')
        slice_index


def remove_chars(sentence, slice_point):
    new_string = sentence[slice_point:]
    print(new_string)


remove_chars(string, slice_index)
