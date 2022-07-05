vowels = ["a", "o", "u", "e", "i"]

print("".join([letter for letter in input() if letter.lower() not in vowels]))