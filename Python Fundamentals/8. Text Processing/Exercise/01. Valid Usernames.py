usernames = input().split(", ")

for username in usernames:

    if 3 <= len(username) <= 16:
        if username.isalnum():
            print(username)

        else:
            if "-" in username or "_" in username:
                print(username)
