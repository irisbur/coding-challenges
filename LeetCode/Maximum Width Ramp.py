from typing import List


def max_width_ramp(nums: List[int]) -> int:
    right_max = []
    cur_max = 0
    for i in range(len(nums) - 1, -1, -1):
        cur_max = max(nums[i], cur_max)
        right_max.append(cur_max)

    right_max.reverse()

    i = 0
    best_ramp = 0
    for j in range(1, len(nums)):
        if i >= j:
            break
        if nums[i] <= nums[j]:
            best_ramp = max(best_ramp, j - i)
        if nums[i] > nums[j] and right_max[j] < nums[i]:
            i += 1

    return best_ramp

