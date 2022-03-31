import re

password_count = int(input())

for i in range(password_count):

    password = input()
    pattern = r"(.+)>(?P<digits>[0-9]{3})\|(?P<lower_letters>[a-z]{3})\|(?P<upper_letters>[A-Z]{3})\|(?P<symbols>.{3}[^<>]*)<(\1)"

    valid = re.match(pattern, password)

    if valid is not None:

        digits = valid.group("digits")
        lower_letters = valid.group("lower_letters")
        upper_letters = valid.group("upper_letters")
        symbols = valid.group("symbols")

        print(f"Password: {digits+lower_letters+upper_letters+symbols}")
    else:
        print("Try another password!")