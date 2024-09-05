from typing import List


def h_index_sort(citations: List[int]) -> int:
    citations.sort()

    for i in range(len(citations)):
        if len(citations) - i <= citations[i]:
            return len(citations) - i
    return 0


def h_index(citations: List[int]) -> int:
    n = len(citations)
    freq = [0 for _ in range(n + 1)]

    for c in citations:
        if c >= n:
            freq[n] += 1
        else:
            freq[c] += 1

    total = 0
    for i in range(n, -1, -1):
        total += freq[i]
        if total >= i:
            return i

    return 0
