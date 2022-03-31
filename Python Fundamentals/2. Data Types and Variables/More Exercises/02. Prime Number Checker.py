number = int(input())
is_prime = True

for n in range(2, number):

    if number % n == 0:
        print("False")
        is_prime = False
        break

if is_prime:
    print("True")