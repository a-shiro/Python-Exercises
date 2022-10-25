def sort_vips_and_regulars(reservation_list):
    vip_guests = []
    regular_guests = []

    for guest in reservation_list:
        if guest[0].isdigit():
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)

    return sorted(vip_guests), sorted(regular_guests)


n = int(input())

reservation_list = set()

for _ in range(n):
    reservation_list.add(input())

while True:
    guests = input()

    if guests == "END":
        break

    reservation_list.remove(guests)

print(len(reservation_list))
vip, regular = sort_vips_and_regulars(reservation_list)
[print(v) for v in vip]
[print(r) for r in regular]
