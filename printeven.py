# Exercise 3: Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters
# that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

string = input('Enter word: ')


# suppose I don't know the length of the string and I wanna know how long it is
for index in range(len(string)):
    if index % 2 == 0:
        print(index, string[index])

# using enumerate

for index, letter in enumerate(string):
    if index % 2 == 0:
        print(letter)
