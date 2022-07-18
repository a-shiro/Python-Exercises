def find_combinations(combination, word, elements):
    if ''.join(combination) == word:
        print(*combination)
        return

    if ''.join(combination) not in word:
        combination.clear()
        return

    for el1 in elements:
        for el2 in elements:
            combination.append(el1)
            combination.append(el2)

            find_combinations(combination, word, elements)





elements = input().split(', ')
word = input()

find_combinations([], word, elements)


# me, so, do, m, ran
# somerandomtext
