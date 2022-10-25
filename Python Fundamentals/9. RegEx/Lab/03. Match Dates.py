import re

pattern = r"(?P<day>\d{2})([-./])(?P<month>[A-Z][a-z]{2})(\2)(?P<year>\d{4})"
text = input()

valid_dates = re.findall(pattern, text)

for date in valid_dates:

    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[4]}")