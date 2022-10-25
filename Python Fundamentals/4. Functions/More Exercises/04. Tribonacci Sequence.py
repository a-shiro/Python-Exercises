def tribonacci_sequence(numbers_count):

    numbers_list = [0, 0, 0]

    for _ in range(numbers_count):

        trib_num = sum(numbers_list)
        if trib_num == 0:
            trib_num = 1

        numbers_list[0] = numbers_list[1]
        numbers_list[1] = numbers_list[2]
        numbers_list[2] = trib_num

        print(trib_num, end=" ")


numbers_count = int(input())

tribonacci_sequence(numbers_count)

