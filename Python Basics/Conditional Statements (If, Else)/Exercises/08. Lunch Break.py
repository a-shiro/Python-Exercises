import math

series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
chill_time = break_length / 4

time_left = break_length - (lunch_time + chill_time)

if time_left >= episode_length:
    time_left = math.ceil(time_left - episode_length)

    print(f'You have enough time to watch {series_name} and left with {time_left:.0f} minutes free time.')
else:
    time_required = math.ceil(episode_length - time_left)

    print(f"You don't have enough time to watch {series_name}, you need {time_required:.0f} more minutes.")
