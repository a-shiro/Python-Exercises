hour = int(input())
day = input()

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" \
or  day == "Saturday":
    if hour == 10 or hour == 11 or hour == 12 or hour == 13 or hour == 14 or hour == 15 \
        or hour == 16 or hour == 17 or hour == 18:

        print("open")
    else:
        print("closed")

elif day == "Sunday":
    print("closed")
