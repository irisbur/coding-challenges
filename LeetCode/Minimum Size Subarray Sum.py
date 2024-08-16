from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_steps = 0
    l, r = 0, 0
    cur_sum = 0

    while r < len(nums):
        cur_sum += nums[r]

        if cur_sum >= target:
            while cur_sum - nums[l] >= target and l < r:
                cur_sum -= nums[l]
                l += 1

            if min_steps == 0:
                min_steps = r - l + 1
            else:
                min_steps = min(r - l + 1, min_steps)
        r += 1

    return min_steps

print(minSubArrayLen(7, [2,3,1,2,4,3]))