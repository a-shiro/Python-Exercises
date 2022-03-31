num_count = int(input())

p1_num_count = 0
p2_num_count = 0
p3_num_count = 0
p4_num_count = 0
p5_num_count = 0

for i in range(num_count):
    number = int(input())
    if number < 200:
        p1_num_count += 1
    elif 200 <= number < 400:
        p2_num_count += 1
    elif 400 <= number < 600:
        p3_num_count += 1
    elif 600 <= number < 800:
        p4_num_count += 1
    else:
        p5_num_count += 1

print(f"{p1_num_count / num_count * 100:.2f}%")
print(f"{p2_num_count / num_count * 100:.2f}%")
print(f"{p3_num_count / num_count * 100:.2f}%")
print(f"{p4_num_count / num_count * 100:.2f}%")
print(f"{p5_num_count / num_count * 100:.2f}%")