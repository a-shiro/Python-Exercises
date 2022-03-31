# Make this code error free

"""
line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])

line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]

print(numbers_dictionary)
"""

# Working Code

numbers_dictionary = {}

line_1 = input()

while line_1 != "Search":
    number_as_string = line_1

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable must be an integer')

    line_1 = input()

line_2 = input()

while line_2 != "Remove":
    key_to_print = line_2

    try:
        print(numbers_dictionary[key_to_print])
    except KeyError:
        print('Number does not exist in dictionary')

    line_2 = input()

line_3 = input()

while line_3 != "End":
    key_to_remove = line_3

    try:
        del numbers_dictionary[key_to_remove]
    except KeyError:
        print('Number does not exist in dictionary')

    line_3 = input()

print(numbers_dictionary)
