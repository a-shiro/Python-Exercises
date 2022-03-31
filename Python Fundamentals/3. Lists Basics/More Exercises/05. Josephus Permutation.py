from collections import deque

sequence = deque([x for x in input().split()])
k = int(input())

answer = []
count = 0

while sequence:

    count += 1

    if count == k:
        answer.append(sequence.popleft())
        count = 0
    else:
        sequence.append(sequence.popleft())

print(f"[{','.join(answer)}]")