rooms = int(input())

free_chairs = 0
not_enough_chairs = False

for room_number in range(1, rooms + 1):
    chairs, people = input().split()

    if int(people) > len(chairs):
        print(f"{int(people) - len(chairs)} more chairs needed in room {room_number}")
        not_enough_chairs = True
    else:
        free_chairs += len(chairs) - int(people)

if not not_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")