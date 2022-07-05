with open('numbers_1.txt', "r") as to_sum, open('numbers_2.txt', 'r') as to_multiply:

    result = 0
    sum = sum(map(int, to_sum.readlines()))

    for i, n in enumerate(to_multiply):
        result = sum * int(n)
        print(f'Result of number {i+1} = {result}')
