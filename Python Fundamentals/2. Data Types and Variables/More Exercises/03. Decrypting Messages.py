key = int(input())
lines = int(input())

decrypted = ""

for _ in range(lines):

    letter = input()
    decrypted += chr(ord(letter) + key)

print(decrypted)