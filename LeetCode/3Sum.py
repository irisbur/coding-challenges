from typing import List


# correct solution but O(n^2)
def three_sum(nums: List[int]) -> List[List[int]]:
    nums_map = nums_to_map(nums)

    triplets = set()
    for num1 in nums_map:
        for num2 in nums_map:
            if num1 == num2 and len(nums_map[num1]) < 2:
                break

            diff = -1 * (num1 + num2)
            if num1 == num2 and num2 == diff and len(nums_map[num1]) > 2:
                triplets.add(tuple(sorted((num1, num2, diff))))
            elif diff in nums_map:
                if (diff != num1 and diff != num2) or (diff == num1 and diff != num2 and len(nums_map[num1]) > 1) or (diff == num2 and diff != num1 and len(nums_map[num2]) > 1):
                    triplets.add(tuple(sorted((num1, num2, diff))))

    return triplets


def nums_to_map(nums):
    nums_map = {}
    for i in range(len(nums)):
        if nums[i] in nums_map:
            nums_map[nums[i]].append(i)
        else:
            nums_map[nums[i]] = [i]
    return nums_map

print(three_sum([-1,0,1,0]))