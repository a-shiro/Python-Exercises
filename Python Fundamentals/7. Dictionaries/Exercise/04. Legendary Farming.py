def can_craft(for_legendary):

    for resource, qty in for_legendary.items():
        if qty >= 250:
            return True


resources = input().split()

for_legendary = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ""

while True:

    for i in range(0, len(resources), 2):

        qty = int(resources[i])
        name = resources[i + 1].lower()

        if name in for_legendary.keys():
            for_legendary[name] += qty
            if can_craft(for_legendary):
                break
        else:
            if name not in junk.keys():
                junk[name] = qty
            else:
                junk[name] += qty

    if can_craft(for_legendary):
        break
    else:
        resources = input().split()

for resource, qty in for_legendary.items():
    if resource == "shards" and qty >= 250:
        item_obtained = "Shadowmourne"
        for_legendary[resource] -= 250
        break
    elif resource == "fragments" and qty >= 250:
        item_obtained = "Valanyr"
        for_legendary[resource] -= 250
        break
    elif resource == "motes" and qty >= 250:
        item_obtained = "Dragonwrath"
        for_legendary[resource] -= 250
        break

print(f"{item_obtained} obtained!")

sorted_resources = sorted(for_legendary.items(), key=lambda r: (-r[1], r[0]))
sorted_junk = sorted(junk.items(), key=lambda j: j[0])

for tup in sorted_resources:
    print(f"{tup[0]}: {tup[1]}")

for tup in sorted_junk:
    print(f"{tup[0]}: {tup[1]}")