str_1 = input().split(", ")
str_2 = input().split(", ")

my_list = []
for el in str_1:
    for el_2 in str_2:
        if el in el_2:
            my_list.append(el)
            break

print(my_list)