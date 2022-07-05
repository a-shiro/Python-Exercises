sequence = input()

opening_brackets = []
is_balanced = True

for bracket in sequence:

    if bracket in "([{":
        opening_brackets.append(bracket)

    elif bracket in ")]}":

        if not opening_brackets:  # if its empty its unbalanced
            is_balanced = False
            break

        opening_bracket = opening_brackets.pop()

        if bracket == ")":
            if not opening_bracket == "(":
                is_balanced = False
                break
        elif bracket == "]":
            if not opening_bracket == "[":
                is_balanced = False
                break
        elif bracket == "}":
            if not opening_bracket == "{":
                is_balanced = False
                break

if is_balanced and len(opening_brackets) == 0:
    print("YES")
else:
    print("NO")