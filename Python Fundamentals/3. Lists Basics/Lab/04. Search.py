n = int(input())
key_word = input()

my_list = []

for _ in range(n):
    some_strings = input()
    my_list.append(some_strings)

print(my_list)

for i in range(len(my_list) - 1, -1, -1):
    element = my_list[i]
    if key_word not in element:
        my_list.remove(element)

print(my_list)



