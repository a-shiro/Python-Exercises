numbers = [int(n) for n in input().split()]

average_number = sum(numbers) / len(numbers)

answer = []
for n in range(len(numbers) - 1, -1, -1):
    if (len(answer)) == 5:
        break
    if numbers[n] > average_number:
        max_number = max(numbers)
        answer.append(max_number)
        numbers.remove(max_number)

if answer == []:
    print("No")
else:
    print(" ".join([str(n) for n in answer]))
