from collections import deque

expression = input().split()

not_assigned = True
numbers = deque()
total = 0

for el in expression:

    if el.lstrip('-').isdigit():
        numbers.append(int(el))
    else:

        if not_assigned:
            total = numbers.popleft()
            not_assigned = False

        if el == "+":
            for n in range(len(numbers)):
                total += numbers.popleft()
        elif el == "-":
            for n in range(len(numbers)):
                total -= numbers.popleft()
        elif el == "*":
            for n in range(len(numbers)):
                total *= numbers.popleft()
        elif el == "/":
            for n in range(len(numbers)):
                total //= numbers.popleft()

print(total)