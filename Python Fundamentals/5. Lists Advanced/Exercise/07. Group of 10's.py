numbers = [int(num) for num in input().split(", ")]
boundary = 10

answer_list = []
while not numbers == []:
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] <= boundary:
            answer_list.append(numbers[i])
            numbers.remove(numbers[i])
    print(f"Group of {boundary}'s: {(answer_list[::-1])}")
    boundary += 10
    answer_list = []


