from collections import deque
from typing import List


def update_matrix_bfs(mat: List[List[int]]) -> List[List[int]]:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(mat), len(mat[0])

    qe = deque()
    dist_mat = [[float('inf') for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                qe.append((i, j))
                dist_mat[i][j] = 0

    while qe:
        cx, cy = qe.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= cx + dx < m and 0 <= cy + dy < n and dist_mat[nx][ny] == float('inf'):
                qe.append((nx, ny))
                dist_mat[nx][ny] = 0 if mat[nx][ny] == 0 else dist_mat[cx][cy] + 1

    return dist_mat


print(update_matrix_bfs([[1,1,0,0,1,0,0,1,1,0],
                     [1,0,0,1,0,1,1,1,1,1],
                     [1,1,1,0,0,1,1,1,1,0],
                     [0,1,1,1,0,1,1,1,1,1],
                     [0,0,1,1,1,1,1,1,1,0],
                     [1,1,1,1,1,1,0,1,1,1],
                     [0,1,1,1,1,1,1,0,0,1],
                     [1,1,1,1,1,0,0,1,1,1],
                     [0,1,0,1,1,0,1,1,1,1],
                     [1,1,1,0,1,0,1,1,1,1]]))