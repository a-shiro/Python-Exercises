def is_password_between_six_and_ten_chr(password):
    no_error = True
    if not 6 <= len(password) <= 10:
        no_error = False

    return no_error


def is_password_alphanumerical(password):
    no_error = True
    if not password.isalnum():
        no_error = False

    return no_error


def does_password_have_two_digits(password):
    no_error = True
    digit_counter = 0
    for character in password:
        if character.isdigit():
            digit_counter += 1
            if digit_counter == 2:
                break
    if digit_counter < 2:
        no_error = False

    return no_error


password = input()
is_valid = True

if not is_password_between_six_and_ten_chr(password):
    is_valid = False
    print("Password must be between 6 and 10 characters")
if not is_password_alphanumerical(password):
    is_valid = False
    print("Password must consist only of letters and digits")
if not does_password_have_two_digits(password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")


