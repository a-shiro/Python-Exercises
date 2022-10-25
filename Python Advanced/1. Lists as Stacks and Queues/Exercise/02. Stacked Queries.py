lines = int(input())

stack = []

for _ in range(lines):

    command = input().split()

    if command[0] == '1':
        n_to_append = int(command[1])
        stack.append(n_to_append)
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))

while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")