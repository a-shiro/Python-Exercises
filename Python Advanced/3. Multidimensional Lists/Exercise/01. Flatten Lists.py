sublist = [[y for y in x.split(' ')] for x in input().split('|')]

result = []

for row in sublist[::-1]:
    for col in row:
        if not col == '':
            result.append(col)

print(' '.join(result))