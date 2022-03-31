people = int(input())
lift = [int(wagon) for wagon in input().split()]

while people > 0 and sum(lift) < len(lift) * 4:
    people -= 1
    for wagon in range(len(lift)):
        if lift[wagon] < 4:
            lift[wagon] += 1
            break

if sum(lift) < len(lift) * 4:
    print(f"The lift has empty spots!")
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(*lift)