import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

valid_names = re.finditer(pattern, text)
for name in valid_names:
    print(name.group(), end=" ")