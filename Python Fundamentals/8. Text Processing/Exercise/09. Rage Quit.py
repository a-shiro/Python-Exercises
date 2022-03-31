def search(data):

    string = ""
    number = ""
    last_i = ""

    for el in data:

        if el.isdigit():
            number += el
            last_i = data.index(el)
            continue
        elif number == "":
            string += el
        else:
            break

    return string, number, last_i


data = input()

rage_msg = ""
while not data == "":

    string, number, last_i = search(data)

    rage_msg += string.upper() * int(number)

    data = data[last_i + 1:]

unique_sym = set(rage_msg)

print(f"Unique symbols used: {len(unique_sym)}")
print(rage_msg)
