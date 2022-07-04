text = input()

number = 0

for letter in text:
    if letter == "a":
        number += 1
    elif letter == "e":
        number += 2
    elif letter == "i":
        number += 3
    elif letter == "o":
        number += 4
    elif letter == "u":
        number += 5

print(number)
