import re

text = input()
pattern = r"\s[a-z0-9]+[-._]?[a-z0-9]+\@[\-?a-z]+\.[\-?a-z\.]+"

valid_emails = [email for email in re.findall(pattern, text)]

for email in valid_emails:

    valid_email = email.replace(" ", "")

    last_el = email[len(email) - 1]
    if last_el == ".":
        valid_email = valid_email[:len(valid_email) - 1]
        print(valid_email)
    else:
        print(valid_email)

