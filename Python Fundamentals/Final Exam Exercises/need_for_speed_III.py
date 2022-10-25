cars = {}

n = int(input())

for _ in range(n):
    name, mileage, fuel = input().split("|")

    cars[name] = [int(mileage), int(fuel)]

command = input().split(" : ")

while not command[0] == "Stop":

    if command[0] == "Drive":
        car, distance, fuel_needed = command[1], command[2], command[3]

        if int(fuel_needed) <= cars[car][1]:
            cars[car][0] += int(distance)
            cars[car][1] -= int(fuel_needed)
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    elif command[0] == "Refuel":
        car, refill = command[1], command[2]

        if int(refill) + cars[car][1] > 75:
            amount_refuel = 75 - cars[car][1]
            cars[car][1] = 75
        else:
            amount_refuel = refill
            cars[car][1] += int(refill)

        print(f"{car} refueled with {amount_refuel} liters")

    elif command[0] == "Revert":
        car, kilometers = command[1], command[2]

        cars[car][0] -= int(kilometers)

        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input().split(" : ")

cars = sorted(cars.items(), key=lambda x: (-int(x[1][0]), x[0]))

for tup in cars:
    car, mileage, fuel = tup[0], tup[1][0], tup[1][1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

