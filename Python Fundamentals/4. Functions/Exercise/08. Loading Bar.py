number = int(input())
number_left = 10

percent_count = number // 10
number_left -= percent_count
percent_in_output = percent_count * "%"
unloaded_count = number_left * "."

answer = percent_in_output + unloaded_count

if number < 100:
    print(f"{number}% [{answer}]")
    print("Still loading...")

else:
    print("100% Complete!")
    print(f"[{percent_in_output}]")