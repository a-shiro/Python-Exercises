first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

n_lines = int(input())

for _ in range(n_lines):

    command = input().split()

    if command[0] == "Add":
        if command[1] == "First":
            add_num_in_first_seq = set(int(n) for n in command[2:])

            for n in add_num_in_first_seq:
                first_sequence.add(n)

        elif command[1] == "Second":
            add_num_in_second_seq = set(int(n) for n in command[2:])

            for n in add_num_in_second_seq:
                second_sequence.add(n)

    elif command[0] == "Remove":
        if command[1] == "First":
            remove_num_in_first_seq = set(int(n) for n in command[2:])

            for n in remove_num_in_first_seq:
                first_sequence.discard(n)

        elif command[1] == "Second":
            remove_num_in_second_seq = set(int(n) for n in command[2:])

            for n in remove_num_in_second_seq:
                second_sequence.discard(n)

    else:
        if first_sequence.issubset(second_sequence):
            print("True")
        elif second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(', '.join(map(str, sorted(first_sequence))))
print(', '.join(map(str, sorted(second_sequence))))
