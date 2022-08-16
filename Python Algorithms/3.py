values = input().split('?')

commands = []
numbers = []
for el in values:
    if el.strip() == 't' or el.strip() == 'f':
        commands.append(el.strip())

for x in values:
    if ':' in x:
        numbers = [el.strip() for el in x.split(':')]

while commands:
    command = commands.pop()

    if command == 't':
        numbers.remove(numbers[1])

    elif command == 'f':
        numbers.remove(numbers[0])

print(*numbers)

# t ? 4 : 2
# f ? 4 : 2
# f ? f ? 4 : 2
# t ? t ? t ? f ? f ? 4 : 1 : 2 : 3 : 10 : 12
#
# t ? f ? t ? 4 : 1 : 2 : 3

# (f (f (t (t (t 4 : 1) : 2) : 3) : 10) : 12))

# f ? f ? 4 : 2 : 1