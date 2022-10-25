fire_info = input().split("#")
water_amount = int(input())

effort = 0
fire_put_out = []

for i in fire_info:
    fire_type_and_range = i.split(" = ")

    fire_type = fire_type_and_range[0]
    fire_range = int(fire_type_and_range[1])

    if fire_type == "High" and 81 <= fire_range <= 125:
        if water_amount >= fire_range:
            water_amount -= fire_range
            effort += 0.25 * fire_range
            fire_put_out.append(fire_range)

    elif fire_type == "Medium" and 51 <= fire_range <= 80:
        if water_amount >= fire_range:
            water_amount -= fire_range
            effort += 0.25 * fire_range
            fire_put_out.append(fire_range)

    elif fire_type == "Low" and 1 <= fire_range <= 50:
        if water_amount >= fire_range:
            water_amount -= fire_range
            effort += 0.25 * fire_range
            fire_put_out.append(fire_range)


print("Cells:")
for i in fire_put_out:
    print(f" - {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {(sum(fire_put_out))}")


