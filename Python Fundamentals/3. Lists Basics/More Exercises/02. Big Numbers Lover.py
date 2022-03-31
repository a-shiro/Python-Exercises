numbers = input().split(" ")
max_number = ''
biggest = sorted(numbers, reverse = True)

for num in biggest:
    max_number += num
print(max_number)