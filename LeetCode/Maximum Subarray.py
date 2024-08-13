
def maxSubArray(nums) -> int:
    max_sum, curr_sum = nums[0], 0

    for i in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

print(maxSubArray([5,4,-1,7,8]))