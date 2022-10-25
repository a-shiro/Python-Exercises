def list_manipulator(list, command_1, command_2, *args):
    if command_1 == 'add':
        if command_2 == 'beginning':
            [list.insert(0, n) for n in args[::-1]]
            return list
        elif command_2 == 'end':
            [list.append(n) for n in args]
            return list
    elif command_1 == 'remove':
        if command_2 == 'beginning':
            if len(args) == 0:
                list.pop(0)
                return list
            [list.pop(0) for _ in range(args[0])]
            return list
        elif command_2 == 'end':
            if len(args) == 0:
                list.pop()
                return list
            [list.pop() for _ in range(args[0])]
            return list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
