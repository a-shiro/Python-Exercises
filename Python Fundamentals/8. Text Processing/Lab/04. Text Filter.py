banned_word = input().split(", ")
text = input()

for word in range(len(banned_word)):

    text = text.replace(banned_word[word], "*" * len(banned_word[word]))

print(text)
