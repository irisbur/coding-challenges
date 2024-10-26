from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    if len(nums) == 1:
        return [nums]

    p_nums = self.permute(nums[:-1])
    perms = []
    for perm in p_nums:
        for i in range(len(perm) + 1):
            cur = perm.copy()
            cur.insert(i, nums[-1])
            perms.append(cur)
    return perms

