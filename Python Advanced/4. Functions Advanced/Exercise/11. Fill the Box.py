def fill_the_box(height, length, width, *args):
    finish_index = args.index('Finish')

    box_capacity = height * length * width
    cubes = sum([x for x in args[:finish_index]])

    if box_capacity - cubes > 0:
        return f'There is free space in the box. You could put {box_capacity - cubes} more cubes.'
    else:
        return f'No more free space! You have {cubes - box_capacity} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, 'Finish'))
print(fill_the_box(10, 10, 10, 40, 'Finish', 2, 15, 30))