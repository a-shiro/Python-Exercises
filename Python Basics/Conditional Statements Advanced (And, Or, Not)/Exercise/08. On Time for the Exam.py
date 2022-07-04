hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving

if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
elif time_of_arriving < time_of_exam - 30:  # else:
    print("Early")

if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f'{time_of_exam - time_of_arriving} minutes before the start')

elif time_of_arriving <= time_of_exam - 60:
    hours = (time_of_exam - time_of_arriving) // 60
    minutes = (time_of_exam - time_of_arriving) % 60

    print(f"{hours}:{minutes:0>2d} hours before the start")

elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f'{time_of_arriving - time_of_exam} minutes after the start')

elif time_of_arriving >= time_of_exam + 60:
    hours = (time_of_arriving - time_of_exam) // 60
    minutes = (time_of_arriving - time_of_exam) % 60

    print(f"{hours}:{minutes:0>2d} hours after the start")