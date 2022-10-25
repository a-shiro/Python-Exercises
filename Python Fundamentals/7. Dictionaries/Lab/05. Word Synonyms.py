n = int(input())

synonym_dict = {}
for _ in range(n):
    key = input()
    value = input()

    if key not in synonym_dict:
        synonym_dict[key] = []
    synonym_dict[key].append(value)

for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")