n = int(input())

even = 0
odd = 0

for i in range(n):
    number = int(input())
    if i % 2 == 0:
      even = even + number
    else:
      odd = odd + number

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {abs(even - odd)}")