command = input()

sum_prime = 0
sum_nonprime = 0

while command != "stop":
    num = int(command)
    is_prime = True

    if num == 1:
        command = input()
        continue

    if num < 0:
        print("Number is negative.")
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime += num
        else:
            sum_nonprime += num

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")