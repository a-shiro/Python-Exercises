# First Solution:
# def reverse_numbers(idx, numbers, result):
#     if idx > len(numbers) - 1:
#         return
#
#     reverse_numbers(idx + 1, numbers, result)
#
#     result.append(numbers[idx])
#
#     if len(numbers) == len(result):
#         return result
#
#
# numbers = input().split(' ')
# result = reverse_numbers(0, numbers, [])
#
# print(*result)


# Second Solution:
def reverse_collection(collection, idx):
    if idx == len(collection) - 1:
        return collection[idx]

    return reverse_collection(collection, idx + 1) + ' ' + collection[idx]


collection = input().split(' ')

result = reverse_collection(collection, 0)
print(result)
