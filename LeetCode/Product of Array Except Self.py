from typing import List


# 0(n) runtime complexity and O(n) space complexity solution.
def product_except_self(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    res = [1 for _ in range(len(nums))]
    pre = [1 for _ in range(len(nums))]
    post = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        pre[i] = pre[i - 1] * nums[i]
        post[i] = post[i - 1] * nums[-i - 1]
    print(pre)
    print(post)
    for i in range(len(nums)):
        if i == 0:
            res[i] = post[-2]
        elif i == len(nums) - 1:
            res[i] = pre[i - 1]
        else:
            res[i] = pre[i - 1] * post[len(nums) - i - 2]
    return res


# 0(n) runtime complexity and 0(1) space complexity solution.
def better_product_except_self(nums: List[int]) -> List[int]:
    l, r = 1, 1
    res = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        res[i] *= r
        r *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= l
        l *= nums[i]
    return res


print(better_product_except_self([4, 3, 2, 1, 2]))
