import heapq
from typing import List

def k_closest_with_sort(points: List[List[int]], k: int) -> List[List[int]]:
    points_and_distances = [[x**2 + y ** 2, x, y] for x, y in points]
    points_and_distances.sort(key=lambda x: x[0])
    return [[x, y] for _, x, y in points_and_distances[:k]]


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # idea: to each point calculate the distance of it from origin
    # then create a max heap for the k smallest values
    max_heap = []

    for x, y in points:
        d = x ** 2 + y ** 2
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-1 * d, x, y))
        elif d < -1 * max_heap[0][0]:
            heapq.heapreplace(max_heap, (-1 * d, x, y))
    result = [[x, y] for _, x, y in max_heap]
    return result



print(kClosest([[2,2],[2,2],[3,3],[2,-2],[1,1]],
               4))