numbers = [int(x) for x in input().split()]
numbers.sort()

targeted_number = int(input())


def binary_search(nums, target):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        middle_idx = (left_pointer + right_pointer) // 2
        middle_element = nums[middle_idx]

        if middle_element == targeted_number:
            return middle_idx

        if target > middle_element:
            left_pointer = middle_idx + 1
        else:
            right_pointer = middle_idx - 1

    return -1


print(binary_search(numbers, targeted_number))