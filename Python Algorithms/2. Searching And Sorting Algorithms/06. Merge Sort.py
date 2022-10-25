def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))

    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    middle_idx = len(numbers) // 2
    left = numbers[:middle_idx]
    right = numbers[middle_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = [int(n) for n in input().split()]

result = merge_sort(numbers)

print(*result)