destination = input()
package_type = input()
vip = input()
days = int(input())

total = 0

if destination != "Bansko" and destination != "Borovets" and destination != "Varna" and destination != "Burgas":
    print("Invalid input!")

elif package_type != "withEquipment" and package_type != "noEquipment" and package_type != "withBreakfast" and \
     package_type != "noBreakfast":
    print("Invalid input!")

elif days < 1:
    print("Days must be positive number!")

else:
    if destination == "Bansko" or destination == "Borovets" or destination == "Varna" or destination == "Burgas":

        if package_type == "withEquipment":
            total = days * 100
            if days > 7:
                total -= 100

        elif package_type == "noEquipment":
            total = days * 80
            if days > 7:
                total -= 80

        elif package_type == "withBreakfast":
            total = days * 130
            if days > 7:
                total -= 130

        elif package_type == "noBreakfast":
            total = days * 100
            if days > 7:
                total -= 100

        if  vip == "yes" and package_type == "withEquipment":
            total = total - (total * 0.10)

        elif vip == "yes" and package_type == "noEquipment":
            total = total - (total * 0.05)

        elif vip == "yes" and package_type == "withBreakfast":
            total = total - (total * 0.12)

        elif vip == "yes" and package_type == "noBreakfast":
            total = total - (total * 0.07)

        print(f"The price is {total:.2f}lv! Have a nice time!")


