# Given an integer array nums, rotate the array to the right by k steps,
# where k is non-negative.
from typing import List


def rotate1(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    new = nums[n - k:] + nums[:n - k]
    nums[:] = new


def rotate2(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.reverse()
    n = len(nums)
    k = k % n
    for i in range(k // 2):
        nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

    for i in range((n - k) // 2):
        nums[k + i], nums[n - i - 1] = nums[n - i - 1], nums[k + i]