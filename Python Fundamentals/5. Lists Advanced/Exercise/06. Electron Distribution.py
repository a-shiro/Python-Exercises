electrons = int(input())
shell_position = 0

shells_filled = []

while not electrons == 0:
    shell_position += 1
    shell_max_capacity = 2 * (shell_position ** 2)
    if electrons < shell_max_capacity:
        shell_max_capacity = electrons

    electrons -= shell_max_capacity
    shells_filled.append(shell_max_capacity)

print(shells_filled)



