text = input()

last_char = ""
for char in text:

    if not char == last_char:
        print(char, end="")
        last_char = char