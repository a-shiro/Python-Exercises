import sys
number_count = int(input())

max_number = -sys.maxsize
sum = 0

for each_num in range(number_count):
    number = int(input())

    if number > max_number:
        max_number = number

    sum += number

total_sum = sum - max_number

if max_number == total_sum:
    print("Yes")
    print(f"Sum = {max_number}")

else:
    print("No")
    print(f"Diff = {abs(max_number - total_sum)}")