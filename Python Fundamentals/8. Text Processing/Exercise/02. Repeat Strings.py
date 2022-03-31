sequence = input().split()

answer = ""

for el in sequence:
    answer += el * len(el)

print(answer)