version = [digit for digit in input().split(".")]

update = int("".join(version)) + 1

next_version = ".".join([digit for digit in str(update)])

print(next_version)





