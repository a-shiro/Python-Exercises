from collections import deque

colors_palette = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

string = deque(input().split())

colors_acquired = []

while string:
    if len(string) > 1:
        first = string.popleft()
        last = string.pop()

        color_combo_1 = first + last
        color_combo_2 = last + first

        if color_combo_1 in colors_palette or color_combo_2 in colors_palette:
            if color_combo_1 in colors_palette:
                colors_acquired.append(color_combo_1)
            else:
                colors_acquired.append(color_combo_2)
        else:
            first = first[:-1]
            last = last[:-1]
            middle = len(string) // 2

            if last:
                string.insert(middle, last)
            if first:
                string.insert(middle, first)
    elif len(string) == 1:
        if string[0] in colors_palette:
            colors_acquired.append(string.pop())
        else:
            string.pop()

result = []

for color in colors_acquired:
    if color == 'orange':
        if 'red' in colors_acquired and 'yellow' in colors_acquired:
            result.append(color)
    elif color == 'purple':
        if 'red' in colors_acquired and 'blue' in colors_acquired:
            result.append(color)
    elif color == 'green':
        if 'yellow' in colors_acquired and 'blue' in colors_acquired:
            result.append(color)
    else:
        result.append(color)

print(result)