text = input()

for char in text:
    encrypting = ord(char) + 3
    print(chr(encrypting), end="")