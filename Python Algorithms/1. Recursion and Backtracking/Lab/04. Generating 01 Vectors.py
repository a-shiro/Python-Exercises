def generate_01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        generate_01(idx + 1, vector)


n = int(input())
vector = [None] * n

generate_01(0, vector)