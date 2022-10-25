import copy

text = [el for el in input()]
deepcopy_list = copy.deepcopy(text)

answer = []
previous_el = deepcopy_list[0]
to_add = 0
index = 0

while not deepcopy_list == []:

    if previous_el == ">":
        previous_el = deepcopy_list[0]
        index -= 1
        explosion = int(deepcopy_list[0])
        if to_add > 0:
            explosion += to_add
        while not deepcopy_list[0] == ">":
            deepcopy_list.pop(0)
            explosion -= 1
            if explosion == 0:
                break
            if deepcopy_list == []:
                break
        if explosion > 0:
            to_add += explosion
    else:
        answer.append(deepcopy_list[0])
        deepcopy_list.remove(deepcopy_list[0])
        previous_el = answer[index]

    index += 1

print("".join(answer))

