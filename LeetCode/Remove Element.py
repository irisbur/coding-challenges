from typing import List


def remove_element(nums: List[int], val: int) -> int:
    i, n = 0, len(nums)

    while i < n:
        if nums[i] == val:
            n -= 1
            nums[i], nums[n] = nums[n], nums[i]
        else:
            i += 1
    return n

print(remove_element([4, 5], 4))


# Another working solution, it's the same but a bit less clean
# i, k = 0, 0
# n = len(nums)
#
# while i < n - k:
#     if nums[i] == val:
#         while i < n - k - 1 < n and nums[n - k - 1] == val:
#             k += 1
#         if i < n - 1 - k < n:
#             nums[i], nums[n - k - 1] = nums[n - k - 1], nums[i]
#         k += 1
#
#     i += 1
#
# return len(nums) - k