def find_sum_galaxies_length():
    with open("input.txt", "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
        sum_length = 0

        updated_grid, galaxies, empty_lines, empty_cols = find_galaxies(grid)

        for i, (x1, y1) in enumerate(galaxies):
            for x2, y2 in galaxies[i + 1:]:
                dist = abs(x1 - x2) + abs(y1 - y2)

                for l in empty_lines:
                    if min(x1, x2) < l < max(x1, x2):
                        dist += 999999

                for c in empty_cols:
                    if min(y1, y2) < c < max(y1, y2):
                        dist += 999999

                sum_length += dist

        return sum_length


def find_galaxies(grid):
    empty_lines = [i for i, line in enumerate(grid) if set(line) == {'.'}]

    empty_cols = []
    for j in range(len(grid[0])):
        if all(grid[i][j] == '.' for i in range(len(grid))):
            empty_cols.append(j)

    galaxies = [(i, j) for i, line in enumerate(grid) for j, c in enumerate(line) if c == '#']

    return grid, galaxies, empty_lines, empty_cols


print(find_sum_galaxies_length())
