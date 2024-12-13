

def parse_input():
    with (open('input.txt') as f):
        matrix = [[c for c in l[:-1]] for l in f.readlines()]
        return matrix


def count_guard_steps(grid):
    n, m = len(grid), len(grid[0])
    dir_map = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    next_dir = {"^": ">", ">": "v", "v": "<", "<": "^"}
    count = n*m
    i, j = find_starting_position(grid)
    direction = grid[i][j]

    while count > 0:
        di, dj = dir_map[direction]
        if is_valid_coord(i+di, j+dj, n, m) and grid[i+di][j+dj] == "#":
            direction = next_dir[direction]
            continue

        i, j = i + di, j +  dj

        if not is_valid_coord(i, j, n, m):
            break
        count -= 1

    return count


def find_path(grid):
    n, m = len(grid), len(grid[0])
    dir_map = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    next_dir = {"^": ">", ">": "v", "v": "<", "<": "^"}
    path = []
    i, j = find_starting_position(grid)
    direction = grid[i][j]

    while True:
        di, dj = dir_map[direction]
        if is_valid_coord(i+di, j+dj, n, m) and grid[i+di][j+dj] == "#":
            direction = next_dir[direction]
            continue

        i, j = i + di, j +  dj


        if not is_valid_coord(i, j, n, m):
            break
        path.append([i, j])

    return path


def find_starting_position(grid):
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                return i, j
    return -1, -1

def is_valid_coord(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def count_obstruction_positions():
    grid = parse_input()
    pos_options = set()
    path = find_path(grid)
    for i, j in path:
        if grid[i][j] == ".":
            original = grid[i][j]
            grid[i][j] = "#"
            is_loop = count_guard_steps(grid) == 0
            grid[i][j] = original
            if is_loop:
                pos_options.add((i, j))

    return len(pos_options)


if __name__ == '__main__':
    print(count_obstruction_positions())