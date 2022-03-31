budget = float(input())
one_kg_flour_price = float(input())

egg_pack_price = one_kg_flour_price * 0.75
one_litre_milk_price = one_kg_flour_price * 1.25 / 4

cozonac_cost = one_kg_flour_price + one_litre_milk_price + egg_pack_price

cozonacs_count = 0
colored_eggs_count = 0

while budget >= cozonac_cost:

    budget -= cozonac_cost

    cozonacs_count += 1
    colored_eggs_count += 3

    if cozonacs_count % 3 == 0:
        colored_eggs_count -= cozonacs_count - 2



print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")




