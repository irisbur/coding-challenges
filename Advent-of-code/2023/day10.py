# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this
# North -1, South 1, West -1 , East 1

next_step_dict = {
    '|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)], 'F': [(-1, 0), (0, -1)]
}


def find_farthermost_point():
    with (open("input.txt", "r") as input_file):
        grid = [list(line[:-1]) for line in input_file.readlines()]
        start1, start2 = find_start(grid)
        step1 = find_next_steps(grid, None, start1)
        step2 = find_next_steps(grid, None, start2)
        prev1, prev2 = start1, start2
        steps = 1
        while step1 != step2:
            steps += 1
            step1 = find_next_steps(grid, prev1, step1)
            step2 = find_next_steps(grid, prev2, step2)
            prev1, prev2 = step1, step2

        print(steps)


def find_next_steps(grid, prev_pos, current_pos):
    return 0, 0


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j
    return -1, -1

if __name__ == "__main__":
    find_farthermost_point()
