sequence = input().split(", ")

my_dict = {}

for el in sequence:
    ascii_number = ord(el)
    if el not in my_dict:
        my_dict[el] = ascii_number

print(my_dict)