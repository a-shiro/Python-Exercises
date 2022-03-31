factor = int(input())
count = int(input())

my_list = []

for num in range(1, count + 1):
    number = num * factor
    if number % factor == 0:
        my_list.append(number)

print(my_list)