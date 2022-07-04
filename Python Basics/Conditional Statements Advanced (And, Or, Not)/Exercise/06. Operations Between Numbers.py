n1 = int(input())
n2 = int(input())
symbol = input()

result = 0
devision_by_zero = 1

if symbol == "+":
    result = n1 + n2

elif symbol == "-":
    result = n1 - n2

elif symbol == "*":
    result = n1 * n2

elif symbol == "/":
    if n2 == 0:
        devision_by_zero = 0
    else:
       result = n1 / n2

elif symbol == "%":
    if n2 == 0:
        devision_by_zero = 0
    else:
        result = n1 % n2

if symbol == "+" or symbol == "-" or symbol == "*":
    if result % 2 == 0:
        type = "even"
    else:
        type = "odd"
    print(f"{n1} {symbol} {n2} = {result} - {type}")

elif symbol == "/":
    if devision_by_zero == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} {symbol} {n2} = {result:.2f}")

elif symbol == "%":
    if devision_by_zero == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} {symbol} {n2} = {result}")


