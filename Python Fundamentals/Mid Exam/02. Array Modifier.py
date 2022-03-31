numbers = [int(n) for n in input().split()]
command = input().split()

while not command[0] == "end":

    if command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

    elif command[0] == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])

        numbers[index_1] *= numbers[index_2]

    elif command[0] == "decrease":
        for n in range(len(numbers)):
            numbers[n] -= 1

    command = input().split()

numbers = [str(n) for n in numbers]
print(", ".join(numbers))

