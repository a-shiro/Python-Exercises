n = int(input())

parking_lot = set()

for _ in range(n):
    command, car = input().split(", ")

    if command == "IN":
        parking_lot.add(car)
    elif command == "OUT":
        parking_lot.remove(car)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")

