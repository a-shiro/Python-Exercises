import re

text = input()

valid_matches = []

while text:

    pattern = r"\d+"
    valid_matches += re.findall(pattern, text)

    text = input()

print(*valid_matches)