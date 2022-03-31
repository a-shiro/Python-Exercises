tab_count = int(input())
salary = int(input())

for i in range(tab_count):
    websites = input()

    if websites == "Facebook":
        salary -= 150
    elif websites == "Instagram":
        salary -= 100
    elif websites == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")

else:
    print(salary)