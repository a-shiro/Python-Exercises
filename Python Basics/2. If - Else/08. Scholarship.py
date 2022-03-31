import math

income = float(input())
grade = float(input())
minimum_wage = float(input())


if grade >= 5.5:
    full_scholarship = grade * 25
    print(f"You get a scholarship for excellent results {math.floor(full_scholarship)} BGN")

elif income < minimum_wage and grade > 4.5:
     social_scholarship = minimum_wage * 0.35
     print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")

else:
    print("You cannot get a scholarship!")
