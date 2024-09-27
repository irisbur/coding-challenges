from typing import List


def num_islands(grid: List[List[str]]) -> int:
    num_islands = 0
    n, m = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ones = find_all_ones(grid)

    if not ones:
        return 0
    fi, fj = ones[0]
    current_island = [(fi, fj)]
    visited = {(fi, fj)}
    while ones:
        while current_island:
            ci, cj = current_island.pop()
            ones.remove((ci, cj))
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if is_valid_index(ni, nj, n, m) and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    if grid[ni][nj] == '1':
                        current_island.append((ni, nj))
        num_islands += 1
        if ones:
            current_island = [ones[0]]
            visited.add(ones[0])

    return num_islands


def is_valid_index(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def find_all_ones(grid):
    ones = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                ones.append((i, j))
    return ones
