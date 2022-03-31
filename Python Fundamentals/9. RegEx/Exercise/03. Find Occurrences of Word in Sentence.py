import re

text = input().lower()
word = input().lower()

pattern = rf"\b{word}\b"

valid_matches = len(re.findall(pattern, text))

print(valid_matches)