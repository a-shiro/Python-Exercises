n = int(input())

even_set = set()
odd_set = set()

for row in range(1, n + 1):

    name = input()
    number = 0

    for ch in name:
        number += ord(ch)

    number //= row

    if number % 2 == 0:
        even_set.add(number)
    else:
        odd_set.add(number)

if sum(even_set) == sum(odd_set):
    print(', '.join(map(str, even_set.union(odd_set))))
elif sum(odd_set) > sum(even_set):
    print(', '.join(map(str, odd_set.difference(even_set))))
elif sum(even_set) > sum(odd_set):
    print(', '.join(map(str, even_set.symmetric_difference(odd_set))))
