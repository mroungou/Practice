# Exercise 6: Display numbers divisible by 5 from a list

# Iterate the given list of numbers and print only those numbers which are divisible by 5

def divideby5(integers):
    print(f"Given list {integers}")
    print('Divible by 5')
    for number in integers:
        if number % 5 == 0:
            print(number)


divideby5([12, 9, 10, 5, 15])
