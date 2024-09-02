from typing import List


# Now the runtime complexity is O(n) where n is the length of chalk.
def chalk_replacer_faster(chalk: List[int], k: int) -> int:
    total_chalk = sum(chalk)
    k = k % total_chalk
    for i in range(len(chalk)):
        if k < chalk[i]:
            return i
    return -1


# Naive approach, too slow.
# O(n * (1 + k // sum(chalk))) where n is len(chalk).
def chalk_replacer(chalk: List[int], k: int) -> int:
    n = len(chalk)
    i = 0
    k -= chalk[i]
    while k >= 0:
        i = (i + 1) % n
        k -= chalk[i]
    return i
