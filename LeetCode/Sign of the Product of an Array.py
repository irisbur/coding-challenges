from typing import List


def array_sign(nums: List[int]) -> int:
    sign = 1

    for num in nums:
        if num > 0:
            sign *= 1
        elif num < 0:
            sign *= -1
        else:
            return 0
    return sign
