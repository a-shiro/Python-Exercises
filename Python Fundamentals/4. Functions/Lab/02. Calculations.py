def calculation(operator,n_1,n_2):
    if operator == "multiply":
        return n_1 * n_2
    elif operator == "divide":
        return n_1 // n_2
    elif operator == "add":
        return n_1 + n_2
    elif operator == "subtract":
        return n_1 - n_2

operator = input()
n_1 = int(input())
n_2 = int(input())

print(calculation(operator,n_1,n_2))