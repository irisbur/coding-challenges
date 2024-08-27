
def majority_element(nums) -> int:
    # Boyer Moore voting algorithm.
    count = 0
    res = 0

    for num in nums:
        if count == 0:
            res = num
            count += 1
        elif num == res:
            count += 1
        else:
            count -= 1
    return res
