
# This solution runs in O(1) space and in one pass, giving O(n) time.
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i, num in enumerate(nums):
        if i > 0 and num > nums[i-1]:
            nums[k] = num
            k += 1
    return k
