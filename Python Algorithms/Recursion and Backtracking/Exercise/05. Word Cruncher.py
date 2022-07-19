def find_all_combinations(idx, target_word, words_count, words_by_idx, used_words):
    if idx >= len(target_word):
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue

        used_words.append(word)
        words_count[word] -= 1

        find_all_combinations(idx + len(word), target_word, words_count, words_by_idx, used_words)

        used_words.pop()
        words_count[word] += 1


words = input().split(', ')
target_word = input()

words_count = {}
words_by_idx = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target_word.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)

            idx += len(word)
    except ValueError:
        pass

find_all_combinations(0, target_word, words_count, words_by_idx, [])

# text, me, so, do, m, ran
# somerandomtext

# Word, cruncher, cr, h, unch, c, r, un, ch, er
# Wordcruncher

# tu, stu, p, i, d, pi, pid, s, pi
# stupid
