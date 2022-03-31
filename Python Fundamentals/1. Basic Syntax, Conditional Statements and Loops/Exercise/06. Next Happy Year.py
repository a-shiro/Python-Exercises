current_year = int(input())

while True:
    current_year += 1
    if len(str(current_year)) == len(set(str(current_year))):
        break

print(current_year)