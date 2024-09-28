from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    islands_count = 0
    n, m = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    def bfs(i, j):
        q = deque([(i, j)])
        visited.add((i, j))

        while q:
            ci, cj = q.popleft()

            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if (0 <= ni < n) and (0 <= nj < m) and (grid[ni][nj] == '1') and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs(i, j)
                islands_count += 1

    return islands_count
