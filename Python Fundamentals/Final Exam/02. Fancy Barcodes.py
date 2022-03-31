import re

barcodes_count = int(input())
pattern = r"@[#]+(?P<item>[A-Z][A-Za-z0-9]{4,}[A-Z])@[#]+"

for _ in range(barcodes_count):

    barcode = input()
    match = re.match(pattern, barcode)

    product_code = ""
    has_digit = False

    if match is not None:

        item = match.group("item")
        for char in item:
            if char.isdigit():
                product_code += char
                has_digit = True

        if has_digit:
            print(f"Product group: {product_code}")
        else:
            print(f"Product group: {'00'}")
    else:
        print("Invalid barcode")