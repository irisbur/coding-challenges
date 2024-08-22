from collections import deque
from typing import List


def update_matrix_bfs(mat: List[List[int]]) -> List[List[int]]:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sx, sy = find_initial_coord(mat)
    m, n = len(mat), len(mat[0])

    qe = deque([(sx, sy)])
    visited = {(sx, sy): 0}

    while qe:
        cx, cy = qe.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= cx + dx < m and 0 <= cy + dy < n and (nx, ny) not in visited:
                qe.append((nx, ny))
                visited[(nx, ny)] = 0 if mat[nx][ny] == 0 else visited[cx, cy] + 1
            elif 0 <= cx + dx < m and 0 <= cy + dy < n and (nx, ny) in visited:
                if visited[(nx, ny)] > visited[(cx, cy)] + 1:
                    visited[(nx, ny)] = visited[(cx, cy)] + 1
                    qe.append((nx, ny))

    # turn visited into the new mat
    return create_dist_mat(m, n, visited)


def create_dist_mat(m, n, visited):
    dist_mat = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            dist_mat[i][j] = visited[(i, j)]
    return dist_mat


def find_initial_coord(mat):
    m, n = len(mat), len(mat[0])
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                return i, j
    return -1, -1

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