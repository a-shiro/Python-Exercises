# Fix the code
numbers_list = input().split(", ")

result = 0

for i in range(numbers_list):

    number = numbers_list[i + 1]

    if number < 5:
        result *= number
    elif number > 5 and number > 10:
        result /= number

print(result)


# Working code

numbers_list = map(int, input().split(", "))

result = 1

for n in numbers_list:

    if n <= 5:
        result *= n
    elif n > 5:
        result /= n

print(result)
