from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    out = []
    subset = []

    def dfs(start):
        out.append(subset.copy())
        for i in range(start, len(nums)):
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

    dfs(0)
    return out


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    all_subsets = []

    def dfs(start, current, total):
        if total == target:
            all_subsets.append(current.copy())
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            dfs(i + 1, current, total + candidates[i])
            current.pop()

    dfs(0, [], 0)
    return all_subsets
