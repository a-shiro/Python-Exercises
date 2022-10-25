numbers = [int(n) for n in input().split(", ")]

positive = ", ".join([str(n) for n in numbers if n >= 0])
negative = ", ".join([str(n) for n in numbers if n < 0])
even = ", ".join([str(n) for n in numbers if n % 2 == 0])
odd = ", ".join([str(n) for n in numbers if not n % 2 == 0])

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")