
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


# Part 2, remove some duplicates in-place such that each unique element appears at most twice.
# This solution runs in O(1) space and in one pass, giving O(n) time.
def remove_duplicates2(nums):
    if not nums:
        return 0
    dup_count = 0
    rep_ind = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            dup_count += 1
        if dup_count < 2:
            nums[rep_ind] = nums[i]
            rep_ind += 1
        else:
            dup_count = 0
            nums[rep_ind] = nums[i]
            rep_ind += 1
    return rep_ind
