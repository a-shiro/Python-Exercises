import sys
number_snowballs = int(input())

highest_value = -sys.maxsize
best_snow = 0
best_time = 0
best_quality = 0

for snowballs in range(1, number_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if highest_value < snowball_value:
        highest_value = snowball_value
        best_snow = snowball_snow
        best_time = snowball_time
        best_quality = snowball_quality

print(f"{best_snow} : {best_time} = {highest_value:.0f} ({best_quality})")

