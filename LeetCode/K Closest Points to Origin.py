import heapq
from typing import List

def k_closest_with_sort(points: List[List[int]], k: int) -> List[List[int]]:
    points_and_distances = [[x**2 + y ** 2, x, y] for x, y in points]
    points_and_distances.sort(key=lambda x: x[0])
    return [[x, y] for _, x, y in points_and_distances[:k]]


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # idea: to each point calculate the distance of it from origin
    # then create a max heap for the k smallest values
    distances_dict = {}
    for x, y in points:
        if x**2 + y ** 2 in distances_dict:
            distances_dict[x**2 + y ** 2].append([x, y])
        else:
            distances_dict[x**2 + y ** 2] = [[x, y]]

    k_closest = []
    # push the distance value as the amount of items in that length
    for i, d in enumerate(distances_dict.keys()):
        l = len(distances_dict[d])
        for _ in range(l):
            if len(k_closest) < k:
                heapq.heappush(k_closest, -1 *d)
            elif d < -1* k_closest[0]:
                heapq.heapreplace(k_closest, -1* d)

    k_points = []
    while k_closest:
        points_to_add = distances_dict[-1 * heapq.heappop(k_closest)]
        k_points.extend(points_to_add)
    return k_points[::-1][:k]


print(kClosest([[2,2],[2,2],[3,3],[2,-2],[1,1]],
               4))