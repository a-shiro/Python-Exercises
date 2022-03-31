steps_counter = 0

steps = input()

while steps_counter < 10000:
    if steps == "Going home":
        steps_after_going_home = int(input())
        steps_counter += steps_after_going_home
        break

    else:
        steps = int(steps)
        steps_counter += steps
        if steps_counter >= 10000:
            break
    steps =input()

if steps_counter >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps_counter - 10000} steps over the goal!")

elif steps == "Going home":
    print(f"{10000 - steps_counter} more steps to reach goal.")