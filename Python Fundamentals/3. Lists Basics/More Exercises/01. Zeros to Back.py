numbers = [int(n) for n in input().split(", ")]

zero_count = 0
zeroes = []

for n in numbers:
    if n == 0:
        zero_count += 1
        zeroes.append(0)

while 0 in numbers:
    numbers.remove(0)

numbers.extend(zeroes)

print(numbers)