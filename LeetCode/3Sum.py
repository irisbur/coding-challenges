from typing import List


# correct solution but O(n^2)
def three_sum(nums: List[int]) -> List[List[int]]:
    nums_map = nums_to_map(nums)

    triplets = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = -1 * (nums[i] + nums[j])
            if diff in nums_map:
                idx = [k for k in nums_map[diff] if k != i and k != j]
                for k in idx:
                    triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))

    return triplets


def nums_to_map(nums):
    nums_map = {}
    for i in range(len(nums)):
        if nums[i] in nums_map:
            nums_map[nums[i]].append(i)
        else:
            nums_map[nums[i]] = [i]
    return nums_map


print(three_sum([-1,0,1,2,-1,-4]))