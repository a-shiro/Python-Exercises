def find_answer(numbers, non_numbers):

    skip_list = []
    take_list = []
    to_return = []

    for i in range(len(numbers)): # creates skip and take list
        if i % 2 == 0:
            take_list.append(numbers[i])
        else:
            skip_list.append(numbers[i])

    for i in range(len(skip_list)): # creates the answer

        take = take_list[i]
        skip = skip_list[i]
        to_skip = skip + take

        if take not in range(len(non_numbers)):
            take = len(non_numbers)

        for j in range(take):
            to_return += non_numbers[j]

        if to_skip not in range(len(non_numbers)):
            to_skip = len(non_numbers)

        for _ in range(to_skip):
            non_numbers.pop(0)

    return to_return


string = input()

non_numbers = [char for char in string if not char.isdigit()]
numbers = [int(char) for char in string if char.isdigit()]

answer = find_answer(numbers, non_numbers)

print("".join(answer))