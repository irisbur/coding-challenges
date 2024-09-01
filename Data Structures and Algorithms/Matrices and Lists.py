from typing import List


def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != len(original):
        return []

    res = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(original[i * n + j])
        res.append(row)
    return res