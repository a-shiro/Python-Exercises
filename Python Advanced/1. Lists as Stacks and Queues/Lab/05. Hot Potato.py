kids = input().split()
n_toss = int(input())

while kids:

    if len(kids) == 1:
        print(f"Last is {kids[0]}")
        break

    else:
        for i in range(1, n_toss + 1):
            if i == n_toss:
                name = kids.pop(0)
                print(f"Removed {name}")
            else:
                name = kids.pop(0)
                kids.append(name)