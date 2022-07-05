number = input()

my_list = [n for n in number]
my_list.sort(reverse=True)

print("".join(my_list))