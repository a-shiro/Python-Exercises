number_to_convert = float(input())
type_input = input()
type_output = input()

conversion = f"{type_input}:{type_output}"

if conversion == "mm:cm":
    to_cm = number_to_convert / 10
    print(f"{to_cm:.3f}")

elif conversion == "cm:mm":
    to_mm = number_to_convert * 10
    print(f"{to_mm:.3f}")

elif conversion == "m:cm":
    to_cm = number_to_convert * 100
    print(f"{to_cm:.3f}")

elif conversion == "cm:m":
    to_m = number_to_convert / 100
    print(f"{to_m:.3f}")

elif conversion == "mm:m":
    to_m = number_to_convert / 1000
    print(f"{to_m:.3f}")

elif conversion == "m:mm":
    to_mm = number_to_convert * 1000
    print(f"{to_mm:.3f}")