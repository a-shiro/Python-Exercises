def find_string(data):

    print("$" + data + "$")


def find_int(data):

    print(int(data) * 2)


def find_real(data):

    print(f"{float(data) * 1.5:.2f}")


data_type = input()
data = input()

if data_type == "string":
    find_string(data)
elif data_type == "int":
    find_int(data)
elif data_type == "real":
    find_real(data)
