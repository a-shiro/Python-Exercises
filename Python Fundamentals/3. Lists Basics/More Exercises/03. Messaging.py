numbers = input().split()
string = input()

message = []

for num in numbers:
    index = 0
    for digit in num:
        index += int(digit)

    if index not in range(len(string)):
        index = index - len(string)
        message.append(string[index])
    else:
        message.append(string[index])

    l_half = string[:index]
    r_half = string[index + 1:]

    string = l_half + r_half

print("".join(message))
