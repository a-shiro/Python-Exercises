sequence = [int(x) for x in input().split(' ')]

positive_sum = sum([n for n in sequence if n >= 0])
negative_sum = sum([n for n in sequence if n < 0])

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
