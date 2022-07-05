string = input()

stack = []
result = ""

for ch in string:
    stack.append(ch)

for _ in range(len(stack[::-1])):
    result += stack.pop()

print(result)