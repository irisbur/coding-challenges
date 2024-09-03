from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj_map = {}
    for a, b in prerequisites:
        if a not in adj_map:
            adj_map[a] = [b]
        else:
            adj_map[a].append(b)

    visited = [False] * numCourses
    rec_stack = [False] * numCourses

    for i in range(numCourses):
        if not visited[i] and i in adj_map and has_cycle(adj_map[i], i, visited, rec_stack, adj_map):
            return False
    return True


def has_cycle(adj, i, visited, rec_stack, adj_map):
    if not visited[i]:
        visited[i] = True
        rec_stack[i] = True

        for x in adj:
            if not visited[x] and x in adj_map and has_cycle(adj_map[x], x, visited, rec_stack, adj_map):
                return True
            elif rec_stack[x]:
                return True

    rec_stack[i] = False
    return False


print(canFinish(numCourses=3, prerequisites=[[0, 1], [0, 2], [1, 2]]))
