import math

tournaments_count = int(input())
starting_athlete_points = int(input())

points_this_season = 0
wins = 0

for _ in range(tournaments_count):
    placement = input()

    if placement == 'W':
        points_this_season += 2000
        wins += 1

    elif placement == 'F':
        points_this_season += 1200

    else:
        points_this_season += 720

final_points = starting_athlete_points + points_this_season
average_points = math.floor(points_this_season / tournaments_count)
wins_percentage = wins / tournaments_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{wins_percentage:.2f}%')
