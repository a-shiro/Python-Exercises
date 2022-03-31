start = int(input())
finish = int(input())
magic_number = int(input())

counter = 0
found = False

for i in range(start, finish + 1):
    for j in range(start, finish + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            found = True
            break

    if found == True:
        break

if found == False:
    print(f"{counter} combinations - neither equals {magic_number}")