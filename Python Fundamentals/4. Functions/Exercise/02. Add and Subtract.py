def sum_numbers(n_1,n_2):
    return n_1 + n_2

def subtract(n_3):
    return sum_numbers(n_1,n_2) - n_3

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

print(subtract(n_3))
