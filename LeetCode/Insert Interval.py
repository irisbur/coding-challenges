from typing import List


# runtime complexity in the worst case is O(n^2) where n is the length of the list, because we do the pop()
# inside of the while loop. we can use O(n) space and insert the result to a different list and by doing this
# avoid popping and get O(n) runtime complexity.
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    n = len(intervals)
    i = 0

    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and newInterval[1] >= intervals[i][0]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res
