def lowest_number(n_1,n_2,n_3):
    numbers_list = []

    numbers_list.append(n_1)
    numbers_list.append(n_2)
    numbers_list.append(n_3)

    return numbers_list

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

lowest = lowest_number(n_1,n_2,n_3)

print(min(lowest))