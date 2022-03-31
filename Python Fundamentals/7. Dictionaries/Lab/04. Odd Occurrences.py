string_sequence = input().split()

for index in range(0, len(string_sequence)):
    string_sequence[index] = string_sequence[index].lower()

answer_list = []
for el in string_sequence:
    if el not in answer_list:
        count = string_sequence.count(el)
        if count % 2 == 1:
            answer_list.append(el)

print(" ".join(answer_list))