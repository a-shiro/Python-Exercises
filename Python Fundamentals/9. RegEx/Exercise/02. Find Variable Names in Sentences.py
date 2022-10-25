import re

text = input()
pattern = r"\b_{1}[A-Za-z0-9]+\b"

matches = [match[1:] for match in re.findall(pattern, text)]

print(",".join(matches))