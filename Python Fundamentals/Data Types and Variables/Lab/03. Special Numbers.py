n = int(input())

for number in range(1, n + 1):
    number_to_str = str(number)
    sum_of_digits = 0

    for symbol in number_to_str:
        digit = int(symbol)
        sum_of_digits += digit

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{number} -> True")

    else:
        print(f"{number} -> False")