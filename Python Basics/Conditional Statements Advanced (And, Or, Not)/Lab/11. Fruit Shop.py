fruit = input()
day = input()
quantity = float(input())
if day == "Monday" or day == "Tuesday" or day == "Friday" or day == "Wednesday" or day == "Thursday":
    if fruit == "banana":
        price = quantity * 2.5
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = quantity * 1.2
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = quantity * 0.85
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = quantity * 1.45
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = quantity * 2.7
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = quantity * 5.5
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = quantity * 3.85
        print(f"{price:.2f}")
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = quantity * 2.7
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = quantity * 1.25
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = quantity * 0.9
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = quantity * 1.60
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = quantity * 3
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = quantity * 5.6
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = quantity * 4.2
        print(f"{price:.2f}")

    else:
        print("error")

else:
    print("error")



