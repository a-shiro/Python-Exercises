command = input()
sequence = [int(x) for x in input().split(' ')]

even_or_odd = 0 if command == 'Even' else 1

result = 0
for n in sequence:
    if n % 2 == even_or_odd:
        result += n

print(result * len(sequence))
