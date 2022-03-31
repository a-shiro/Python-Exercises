lines = int(input())

capacity = 225
total_liters = 0

for i in range(lines):
    liters = int(input())
    if liters + total_liters > 255:
        print("Insufficient capacity!")

    else:
        total_liters += liters

print(total_liters)