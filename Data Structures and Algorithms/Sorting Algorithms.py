
def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp


# Recalling sorting algorithms :)
# space complexity O(1), time complexity O(n^2) when n in arr length.
def bubble_sort(arr):
    for i in range(len(arr), 1, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                swap(arr, j-1, j)


# space complexity O(1), time complexity O(n^2) when n in arr length.
def selection_sort(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        swap(arr, smallest_index, i)


# Merge sort algorithm is a divide and conquer algorithm. It's recursive, stable and not an in-place algorithm.
# space complexity is O(n) and time complexity is O(nlogn) where n is the length of the array.
def mergesort(arr):
    temp = [0] * len(arr)
    mergesort_helper(arr, temp, 0, len(arr) - 1)
    return arr


def mergesort_helper(arr, temp, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort_helper(arr, temp, low, mid)
        mergesort_helper(arr, temp, mid + 1, high)
        merge(arr, temp, low, mid, high)


def merge(arr, temp, low, mid, high):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(low, high + 1):
        arr[i] = temp[i]


# Quick sort - a recursive algorithm in which we choose a pivot value and swap between values that are greater then the
# pivot and are lest ro it and values that are smaller then pivot and on the right of the array. We repeat this process
# until the entire array is sorted.
# On average we do log(n) repeats to sort the array so we have O(nlog(n)) time complexity but if our pivot values are
# consistently bad we have worst case time complexity of O(n^2).
# Quicksort has a space complexity of O(log(n)) in the average case.
# This arises from the recursive function calls and the partitioning process.
def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, l, r):
    if l < r:
        pivot = arr[(l+r) // 2]
        index = partition(arr, l, r, pivot)
        quick_sort_helper(arr, l, index - 1)
        quick_sort_helper(arr, index, r)


def partition(arr, l, r, pivot):
    while l <= r:
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l <= r:
            swap(arr, l, r)
            l += 1
            r -= 1
    return l


# Radix sort - has advantage when we have a boundary. e.g when we know a maximal number of bits integer can take.
# we sort each time based on the bits and our run time complexity is O(k*n) where n is the number of elements and
# k is the number of passes of sorting algorithm.
# for radix sort to work properly we need a stable sorting algorithm.
def radix_sort(arr, digit_num):
    max_val = max(arr)

    cur_digit = 1
    while max_val / cur_digit >= 1:
        arr = counting_sort(arr, cur_digit, digit_num)
        cur_digit *= digit_num

    return arr


def counting_sort(arr, cur_digit, digit_num):
    sorted_arr = [0] * len(arr)
    counts = [0] * digit_num
    for num in arr:
        counts[(num // cur_digit) % digit_num] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i - 1] + counts[i]

    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] // cur_digit
        sorted_arr[counts[index % digit_num] - 1] = arr[i]
        counts[index % digit_num] -= 1
    return sorted_arr
