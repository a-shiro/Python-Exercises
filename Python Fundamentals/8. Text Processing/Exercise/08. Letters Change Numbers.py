def data_breakdown(data):
    for el in data:
        number = ""
        first_letter = ""
        second_letter = ""
        for char in el:

            if char.isalpha():
                if first_letter == "":
                    first_letter = char
                else:
                    second_letter = char
            elif char.isdigit():
                number += char

        data.pop(0)
        return number, first_letter ,second_letter


data = input().split()

total_sum = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"

while not data == []:

    number, first_letter, second_letter = data_breakdown(data)

    if first_letter.isupper():
        resulted_num = int(number) / (alphabet.find(first_letter.lower()) + 1)
    else:
        resulted_num = int(number) * (alphabet.find(first_letter.lower()) + 1)

    if second_letter.isupper():
        total_sum += resulted_num - (alphabet.find(second_letter.lower()) + 1)
    else:
        total_sum += resulted_num + (alphabet.find(second_letter.lower()) + 1)

print(f"{total_sum:.2f}")