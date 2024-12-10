

def parse_input():
    with (open('input.txt') as f):
        matrix = [[c for c in l[:-1]] for l in f.readlines()]
        return matrix


def count_guard_steps():
    grid = parse_input()
    n, m = len(grid), len(grid[0])
    dir_map = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    next_dir = {"^": ">", ">": "v", "v": "<", "<": "^"}

    i, j = find_starting_position(grid)
    direction = grid[i][j]
    count = 0

    while True:
        di, dj = dir_map[direction]
        if is_valid_coord(i+di, j+dj, n, m) and grid[i+di][j+dj] == "#":
            direction = next_dir[direction]
            di, dj = dir_map[direction]

        i, j = i + di, j +  dj

        if not is_valid_coord(i, j, n, m):
            break
        print(i, j)

        count += 1



    return count



def find_starting_position(grid):
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                return i, j
    return -1, -1

def is_valid_coord(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

if __name__ == '__main__':
    print(count_guard_steps())