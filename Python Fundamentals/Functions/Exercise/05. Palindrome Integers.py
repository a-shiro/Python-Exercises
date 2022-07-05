def palindrome_integers(positive_numbers):
    answer_list = []
    true_or_false = False
    for current_number in positive_numbers:
        reversing_list = []
        for digit in current_number:
            reversing_list.append(digit)

        reversed_num = "".join(reversed(reversing_list))
        if reversed_num == current_number:
            true_or_false = True
            answer_list.append(true_or_false)
        else:
            true_or_false = False
            answer_list.append(true_or_false)

    return answer_list

positive_numbers = input().split(", ")

answer_list = palindrome_integers(positive_numbers)

for answer in answer_list:
    print(answer)