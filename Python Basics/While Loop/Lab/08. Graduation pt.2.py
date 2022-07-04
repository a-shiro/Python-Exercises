name = input()

grade = float(input())
class_number = 0
failed = 0
grade_sum = 0

while failed < 2:
    class_number += 1

    if 4 <= grade:
       grade_sum  += grade
       if class_number == 12:
           break
       grade = float(input())
    else:
        failed += 1
        if failed == 2:
          break
        grade = float(input())


if class_number == 12:
   print(f"{name} graduated. Average grade: {grade_sum / class_number:.2f}")

else:
    print(f"{name} has been excluded at {class_number - 1} grade")





