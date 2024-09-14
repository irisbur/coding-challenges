from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    fresh, rotten = init_lists(grid)
    visited = set(rotten)

    steps = 0
    while rotten:
        new_rotten = []
        for i, j in rotten:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if is_index_valid(ni, nj, n, m) and (ni, nj) not in visited and grid[ni][nj] == 1:
                    fresh.remove((ni, nj))
                    grid[ni][nj] = 2
                    visited.add((ni, nj))
                    new_rotten.append((ni, nj))
        rotten = new_rotten
        if rotten:
            steps += 1

    if fresh:
        return -1
    else:
        return steps


def is_index_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def init_lists(grid):
    fresh, rotten = [], []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh.append((i, j))
            elif grid[i][j] == 2:
                rotten.append((i, j))
    return fresh, rotten
