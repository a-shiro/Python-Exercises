import re


def get_threshold(text):

    threshold = 1

    for char in text:
        if char.isdigit():
            threshold *= int(char)

    return threshold


text = input()
pattern = r"(::|\*\*)[A-Z][a-z]{2,}(\1)"

threshold = get_threshold(text)
emojis = []

valid_emojis = re.finditer(pattern, text)

for emoji in valid_emojis:
    emojis.append(emoji.group())


print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    coolness = 0
    for char in emoji:
        if char.isalnum():
            coolness += ord(char)
    if coolness >= threshold:
        print(emoji)
