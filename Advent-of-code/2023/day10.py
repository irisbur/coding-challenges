# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this
# North -1, South 1, West -1 , East 1
import math

next_step_dict = {
    '|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)], 'F': [(1, 0), (0, 1)],
    'S': [(1, 0), (0, 1), (-1, 0), (0, -1)],
    '.': []
}


def find_farthermost_point():
    with (open("input.txt", "r") as input_file):
        grid = [list(line[:-1]) for line in input_file.readlines()]
        start = find_start(grid)
        steps = directions_from_start(grid, start)
        prevs = [start] * len(steps)
        steps_count = 1
        while not did_finish_loop(grid, steps):
            steps_count += 1
            steps_that_has_next, nexts = find_next_steps(grid, prevs, steps)
            prevs = steps_that_has_next
            steps = nexts

        return steps_count / 2


def find_next_steps(grid, prevs, steps):
    steps_that_has_next = []
    nexts = []
    for c, (i, j) in enumerate(steps):
        initial_direction = prevs[c][0] - i, prevs[c][1] - j

        if grid[i][j] in ['|', "-"]:
            next_directions = [(k, l) for k, l in next_step_dict[grid[i][j]] if (k, l) != initial_direction]
            next_direction = next_directions[0]
            add_to_next_if_needed(steps_that_has_next, nexts, next_direction, i, j, grid)
        else:
            if initial_direction[0] == 0:
                next_directions = [(k, l) for k, l in next_step_dict[grid[i][j]] if k != 0]
                next_direction = next_directions[0]
                add_to_next_if_needed(steps_that_has_next, nexts, next_direction, i, j, grid)
            else:
                next_directions = [(k, l) for k, l in next_step_dict[grid[i][j]] if k == 0]
                next_direction = next_directions[0]
                add_to_next_if_needed(steps_that_has_next, nexts, next_direction, i, j, grid)
    return steps_that_has_next, nexts


def add_to_next_if_needed(steps_that_has_next, nexts, next_direction, i, j, grid):
    if 0 <= i + next_direction[0] < len(grid) and 0 <= j + next_direction[1] < len(grid[0]):
        nexts.append((i + next_direction[0], j + next_direction[1]))
        steps_that_has_next.append((i, j))


def directions_from_start(grid, start):
    steps_from_start = []
    i, j = start
    for k, l in next_step_dict['S']:
        if 0 <= i + k < len(grid) and 0 <= j + l < len(grid[0]):
            neighbor = grid[i + k][j + l]
            if neighbor != '.':
                steps_from_start.append((i + k, j + l))
    return steps_from_start


def did_finish_loop(grid, steps):
    for i, j in steps:
        if grid[i][j] == 'S':
            return True
    return False


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j
    return -1, -1


if __name__ == "__main__":
    print(find_farthermost_point())
