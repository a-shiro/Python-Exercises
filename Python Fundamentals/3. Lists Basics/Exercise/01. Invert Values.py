numbers = input()

first_list = numbers.split(" ")
second_list = []

for i in range (len(first_list)):

    el = int(first_list[i])

    if el >= 0:
        reversed_value = -1 * el
    else:
        reversed_value = abs(el)

    second_list.append(reversed_value)

print(second_list)


