def find_winner(l_car_time, r_car_time):

    l_car_total = 0
    r_car_total = 0

    for time in l_car_time:
        if time == 0:
            l_car_total *= 0.8
        else:
            l_car_total += time

    for time in r_car_time:
        if time == 0:
            r_car_total *= 0.8
        else:
            r_car_total += time

    if l_car_total < r_car_total:
        print(f"The winner is left with total time: {l_car_total:.1f}")
    elif r_car_total < l_car_total:
        print(f"The winner is right with total time: {r_car_total:.1f}")


numbers = [int(n) for n in input().split()]

l_car_time = numbers[:len(numbers) // 2]
r_car_time = numbers[(len(numbers) // 2) + 1:][::-1]

find_winner(l_car_time, r_car_time)

