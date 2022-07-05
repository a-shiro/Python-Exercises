secret_message = [word for word in input().split()]

secret_message_parts_1 = []
secret_message_parts_2 =[]

for word in secret_message:
    ascii_digits = ""
    for el in word:
        if el.isdigit():
            ascii_digits += el

    secret_message_parts_1.append(chr(int(ascii_digits)))

for word in secret_message:
    word_elements = []
    for el in word:
        word_elements.append(el)
        if el.isdigit():
            word_elements.remove(el)
    secret_message_parts_2.append("".join(word_elements))

current_index = 0
list_in_progress = []
for _ in range(len(secret_message)):
    words_from_sentence = secret_message_parts_1[current_index] + secret_message_parts_2[current_index]
    current_index += 1
    list_in_progress.append(words_from_sentence)

for word in list_in_progress:
    answer = []
    for letter in word:
        answer.append(letter)

    last_index = len(answer) - 1
    answer[1], answer[last_index] = answer[last_index], answer[1]
    print("".join(answer), end=" ")















