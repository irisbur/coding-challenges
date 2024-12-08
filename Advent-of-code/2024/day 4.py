

def parse_input():
    with (open('input.txt') as f):
        matrix = [[c for c in l[:-1]] for l in f.readlines()]
        return matrix

def find_starting_points(matrix, c):
    coords = []
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == c:
                coords.append([i, j])
    return coords

def count_xmas():
    matrix = parse_input()
    n, m = len(matrix), len(matrix[0])

    count = 0
    x_s = find_starting_points(matrix, 'X')
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
    for i, j in x_s:
        for di, dj in directions:
            mi, mj = i + di, j + dj
            ai, aj = i + 2*di, j + 2*dj
            si, sj = i + 3*di, j + 3*dj
            if is_valid_coord(mi, mj, n, m) and is_valid_coord(ai, aj, n, m) and is_valid_coord(si, sj, n, m):
                if matrix[mi][mj] == "M" and matrix[ai][aj] == "A" and matrix[si][sj] == "S":
                    count += 1

    return count

def count_x_mas():
    matrix = parse_input()
    n, m = len(matrix), len(matrix[0])
    count = 0
    a_s = find_starting_points(matrix, 'A')

    for i, j in a_s:
        di1, dj1 = i - 1, j - 1
        di2, dj2 = i - 1, j + 1
        di3, dj3 = i + 1, j - 1
        di4, dj4 = i + 1, j + 1
        if (is_valid_coord(di1, dj1, n, m) and is_valid_coord(di2, dj2, n, m) and is_valid_coord(di3, dj3 , n, m)
                and is_valid_coord(di4, dj4 , n, m)):
            s1 = matrix[di1][dj1] + "A" + matrix[di4][dj4]
            s2 = matrix[di2][dj2] + "A" + matrix[di3][dj3]
            if (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM"):
                count += 1

    return count

def is_valid_coord(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

if __name__ == '__main__':
    print(count_x_mas())