
# Write a function that receives an array of integers
# and returns an array of lists containing the values in the array along with their frequency count.
# The result should be sorted in descending order based on frequencies.
# If values have the same frequency, they should be sorted in ascending order.

def sort_by_frequencies(array):
    array_counter = {}
    for num in array:
        if num in array_counter:
            array_counter[num] += 1
        else:
            array_counter[num] = 1

    frequency_list = [[num, array_counter[num]] for num in array_counter]

    return merge_sort(frequency_list)

# pythonic sort function: output.sort(key=lambda x: (-x[1], x[0]))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1] or (left[i][1] == right[j][1] and left[i][0] < right[j][0]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged
