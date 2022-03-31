numbers =[int(el) for el in input().split( )]
remove_count = int(input())

for _ in range(remove_count):
    numbers.remove(min(numbers))

print(", ".join([str(el) for el in numbers]))

# MY CODE:
# numbers = input().split(" ")
#
# remove_count = int(input())
#
# my_list_int = []
# my_list_str = []
#
# for element in numbers:
#     integer_num = int(element)
#     my_list_int.append(integer_num)
#
# for _ in range(remove_count):
#     my_list_int.remove(min(my_list_int))
#
#
# for element in my_list_int:
#     string_num = str(element)
#     my_list_str.append(string_num)
#
# print(", ".join(my_list_str))



