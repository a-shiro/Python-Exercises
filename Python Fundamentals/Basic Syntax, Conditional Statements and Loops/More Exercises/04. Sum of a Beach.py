string = input().lower()
k_w_total = 0
key_words = ["sand", "water", "fish", "sun"]

for k_w in key_words:
    k_w_total += string.count(k_w)

print(k_w_total)