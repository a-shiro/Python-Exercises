def what_is_it(n_1, n_2, n_3):

    if n_1 == 0 or n_2 == 0 or n_3 == 0:
        print("zero")
    elif n_1 < 0 and n_2 < 0 and n_3 < 0:
        print("negative")
    elif (n_1 < 0 and n_2 < 0) or (n_1 < 0 and n_3 < 0) or (n_2 < 0 and n_3 < 0):
        print("positive")
    elif n_1 < 0 or n_2 < 0 or n_3 < 0:
        print("negative")
    else:
        print("positive")


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

what_is_it(n_1, n_2, n_3)
