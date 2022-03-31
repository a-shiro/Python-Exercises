type = input()
rows = int(input())
columns = int(input())

ticket = 0

if type == "Normal":
    ticket = 7.5

elif type == "Premiere":
    ticket = 12

elif type == "Discount":
    ticket = 5

total_price = ticket * rows * columns

print(f"{total_price:.2f} leva")