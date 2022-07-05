def odd_and_even_sums(numbers):
    even_sum = 0
    odd_sum = 0
    for digit in numbers:

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

numbers = input()
answer = odd_and_even_sums(numbers)

print(answer)