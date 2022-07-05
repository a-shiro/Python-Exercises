def perfect_number(number):

    total_sum = 0

    for n in range(1, number):
        if number % n == 0:
            total_sum += n

    return total_sum


number = int(input())

if perfect_number(number) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")