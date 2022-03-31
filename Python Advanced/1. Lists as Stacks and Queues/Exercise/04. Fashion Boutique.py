clothing_stack = [int(piece) for piece in input().split()]
rack_capacity = int(input())

racks_used = 1
current_rack_capacity = rack_capacity

while clothing_stack:

    piece_of_clothing = clothing_stack[-1]

    if current_rack_capacity < piece_of_clothing:
        racks_used += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= clothing_stack.pop()

print(racks_used)