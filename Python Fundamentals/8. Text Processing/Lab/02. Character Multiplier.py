str = input().split()

total_sum = 0

sum_list_1 = []
sum_list_2 = []

for char in str[0]:
    sum_list_1.append(ord(char))
for char in str[1]:
    sum_list_2.append(ord(char))

if len(sum_list_1) == len(sum_list_2):
    for i in range(len(sum_list_1)):
        total_sum += sum_list_1[i] * sum_list_2[i]
    print(total_sum)

else:
    plus = []
    if len(sum_list_1) > len(sum_list_2):
        for i in range(len(sum_list_1) - 1, -1, -1):
            el = sum_list_1.pop(i)
            plus.append(el)
            if len(sum_list_1) == len(sum_list_2):
                break

        for i in range(len(sum_list_1)):
            total_sum += sum_list_1[i] * sum_list_2[i]
        print(f"{total_sum + sum(plus)}")

    elif len(sum_list_2) > len(sum_list_1):
        for i in range(len(sum_list_2) - 1, -1, -1):
            el = sum_list_2.pop(i)
            plus.append(el)
            if len(sum_list_1) == len(sum_list_2):
                break

        for i in range(len(sum_list_2)):
            total_sum += sum_list_1[i] * sum_list_2[i]
        print(f"{total_sum + sum(plus)}")