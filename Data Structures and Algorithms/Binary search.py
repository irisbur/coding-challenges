def search(nums, target) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def recursive_search(nums, target) -> int:
    return helper_search(nums, target, 0, len(nums) - 1)


def helper_search(nums, target, l, r):
    if l > r:
        return -1
    mid = l + (r - l) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return helper_search(nums, target, l, mid - 1)
    else:
        return helper_search(nums, target, mid + 1, r)


print(search([-1, 0, 3, 5, 7, 9, 12], -1))
