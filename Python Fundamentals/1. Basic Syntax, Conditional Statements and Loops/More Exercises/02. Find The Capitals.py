string = input()
my_list = [i for i in range(len(string)) if string[i].isupper()]
print(my_list)