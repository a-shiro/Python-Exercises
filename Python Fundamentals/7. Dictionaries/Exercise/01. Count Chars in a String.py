my_list = input().split()

my_dict = {}

for el in my_list:
    for char in el:
        if char not in my_dict:
            my_dict[char] = 0

for el in my_list:
    for char in el:
        my_dict[char] += 1

for key in my_dict.keys():
    print(f"{key} -> {my_dict[key]}")