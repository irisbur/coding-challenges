# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this
# North -1, South 1, West -1 , East 1

# Part 1 - Basically implement BFS #
from collections import deque

NEXT_STEP = {
    '|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)], 'F': [(1, 0), (0, 1)],
    'S': [(1, 0), (0, 1), (-1, 0), (0, -1)],
    '.': []
}


def bfs_farthest_point(grid, start):
    queue = deque([start])
    visited = {start: 0}
    max_dist = 0
    edges = []
    while queue:
        i, j = queue.popleft()

        for di, dj in NEXT_STEP[grid[i][j]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '.' and (ni, nj) not in visited:
                back_dir = -di, -dj
                if back_dir in NEXT_STEP[grid[ni][nj]]:
                    visited[(ni, nj)] = visited[(i, j)] + 1
                    queue.append((ni, nj))
                    edges.append(((i, j), (ni, nj)))
                    max_dist = max(max_dist, visited[(i, j)] + 1)

    return list(visited.keys()), edges, max_dist


def find_farthermost_point():
    with open("input.txt", "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
        start = find_start(grid)
        return bfs_farthest_point(grid, start)[1]


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j
    return -1, -1

# Part 2 - Basically implement Ray Casting #


def is_inside(edges, xp, yp):
    cnt = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return cnt % 2 == 1


def count_enclosed_tiles():
    with open("input.txt", "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
        start = find_start(grid)
        vertices = bfs_farthest_point(grid, start)[0]
        edges = bfs_farthest_point(grid, start)[1]
        count_tiles = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in vertices and is_inside(edges, i, j):
                    count_tiles += 1
        return count_tiles


if __name__ == "__main__":
    print(count_enclosed_tiles())
