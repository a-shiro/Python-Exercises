import math

shape = input()
area = 0

if shape == "square":
    a = float(input())
    area = a * a
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif shape == "circle":
    r = float(input())
    area = math.pi * r**2
elif shape == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f"{area:.3f}")
