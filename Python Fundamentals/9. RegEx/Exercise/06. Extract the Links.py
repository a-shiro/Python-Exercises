import re

text = input()
pattern = r"www.[A-Za-z\-*[0-9]+\.[a-z\.*]+"

while not text == "":

    valid_match = re.findall(pattern, text)
    if valid_match:
        print(*valid_match)

    text = input()