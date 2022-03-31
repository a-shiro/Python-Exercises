import re

pattern = r"\+359( |-)2(\1)\d{3}(\1)\d{4}\b"
text = input()

valid_numbers = re.finditer(pattern, text)
nums = [num.group() for num in valid_numbers]

print(", ".join(nums))

