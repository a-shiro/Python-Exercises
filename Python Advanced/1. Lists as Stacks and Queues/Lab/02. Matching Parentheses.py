parentheses = input()

opening = []

for i, ch in enumerate(parentheses):

    if ch == "(":
        opening.append(i)

    elif ch == ")":
        slice_from = opening.pop()
        slice_to = i

        print(parentheses[slice_from:slice_to + 1])
        