
total = 0

command = input()
while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total += money
    command = input()

print(f"Total: {total:.2f}")