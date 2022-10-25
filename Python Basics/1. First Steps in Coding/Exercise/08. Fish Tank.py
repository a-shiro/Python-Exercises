lenght = int(input())
width = int(input())
height = int(input())
percent_used = float(input())

total_aquarium_storage = lenght * width * height
total_aquarium_litres = total_aquarium_storage * 0.001
percent = percent_used * 0.01
needed_litres = total_aquarium_litres * (1 - percent)

print(needed_litres)