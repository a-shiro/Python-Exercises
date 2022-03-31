resource_or_qty = input()

resource_dict = {}
last_resource = ""
input_count = 0

while not resource_or_qty == "stop":
    input_count += 1

    if input_count % 2 == 1:
        last_resource = resource_or_qty
        if resource_or_qty not in resource_dict:
            resource_dict[resource_or_qty] = 0

    elif input_count % 2 == 0:
        resource_dict[last_resource] += int(resource_or_qty)

    resource_or_qty = input()

for key in resource_dict.keys():
    print(f"{key} -> {resource_dict[key]}")