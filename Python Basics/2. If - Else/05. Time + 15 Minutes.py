hours = int(input())
minutes = int(input())

total_minutes = minutes + hours * 60 + 15

new_hours = total_minutes // 60
new_minutes = total_minutes % 60

if new_minutes < 10:
    print(f"{new_hours % 24}:0{new_minutes}")

else:
    print(f"{new_hours % 24}:{new_minutes}")

