
# write a naive solution and then improve it


def find_sum_galaxies_length():
    with open("input.txt", "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
        # grid, galaxies, expended_rows, expended_cols = find_galaxies(grid)
        sum_length = 0
        expend_grid(grid)
        # for i, galaxy in enumerate(galaxies):
        #     dist_mat = find_dists_in_grid(grid, galaxy, expended_rows, expended_cols)
        #     print(dist_mat)


def find_dists_in_grid(grid, start, expended_rows, expended_cols):
    dist_mat = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]  # visited list
    si, sj = start
    dist_mat[si][sj] = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def expend_grid(grid):
    galaxies = []
    # galaxies_count = 0
    expended_rows, expended_cols = {x for x in range(len(grid))}, {x for x in range(len(grid[0]))}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                galaxies.append((i, j))
                # galaxies_count += 1
                # grid[i][j] = galaxies_count
                if i in expended_rows:
                    expended_rows.remove(i)
                if j in expended_cols:
                    expended_cols.remove(j)

    # expend rows

    for i,idx in enumerate(expended_rows):
        grid = grid[:idx + i] + [['.' for _ in range(len(grid[0]))]] + grid[idx + i:]

    # expend cols
    helper = transpose(grid)
    for i,idx in enumerate(expended_cols):
        helper = helper[:idx + i] + [['.' for _ in range(len(grid))]] + helper[idx +i:]
    grid = transpose(helper)

    for line in grid:
        print(''.join(line))

    return grid, galaxies, expended_rows, expended_cols


def transpose(grid): # grid m x n
    transposed_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))] # grid_t m x n
    for i in range(len(transposed_grid)):
        for j in range(len(transposed_grid[0])):
            transposed_grid[i][j] = grid[j][i]
    return transposed_grid


print(find_sum_galaxies_length())
