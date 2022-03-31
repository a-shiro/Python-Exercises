herd = input().split(", ")
sheep_count = 0

if herd[len(herd) - 1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(herd) - 1, -1, -1):
        if sheep_count == 0 and herd[i] == "wolf":
            print("Please go away and stop eating my sheep")
            break
        elif herd[i] == "wolf":
            break
        elif herd[i] == "sheep":
            sheep_count += 1
    print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")