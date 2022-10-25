import re

text = input()
pattern = r"(@|#)(?P<l_half>[A-Za-z]{3,})(\1{2})(?P<r_half>[A-Za-z]{3,})(\1)"
are_mirror = True
mirror_pairs = []
matches_count = 0

matches = re.finditer(pattern, text)

for pair in matches:

    matches_count += 1

    l_half = pair.group("l_half")
    r_half = pair.group("r_half")

    if len(l_half) == len(r_half):
        for i in range(len(l_half)):

            l_char = l_half[i]
            r_char = r_half[len(r_half) - i -1]

            if l_char == r_char:
                are_mirror = True
            else:
                are_mirror = False
                break

        if are_mirror:
            mirror_pairs.append(f"{l_half} <=> {r_half}")

if not matches_count == 0:
    print(f"{matches_count} word pairs found!")
else:
    print("No word pairs found!")

if not mirror_pairs == []:
    print("The mirror words are:")
    print(f"{', '.join(mirror_pairs)}")
else:
    print("No mirror words!")