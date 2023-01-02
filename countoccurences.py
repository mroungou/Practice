# Exercise 7: Return the count of a given substring from a string

# Write a program to find how many times substring “Emma” appears in the given string.

# Given:

# str_x = "Emma is good developer. Emma is a writer"

sentence = "Emma is a good developer. Emma is a writer"

# print(sentence.find("Emma"))
words = sentence.split()
occurence = 0
for word in words:
    if word == "Emma":
        occurence += 1
print(f'Emma appeared {occurence} times')

# alternatively string.count() could have been used
cnt = sentence.count("Emma")
print(cnt)
