

def parse_input():
    with (open('input.txt') as f):
        matrix = [[c for c in l[:-1]] for l in f.readlines()]
        return matrix

def map_antennas(grid):
    antennas = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                if grid[i][j] in antennas:
                    antennas[grid[i][j]].append([i,j])
                else:
                    antennas[grid[i][j]] = [[i, j]]
    return antennas

def count_antinodes():
    grid = parse_input()
    n, m = len(grid), len(grid[0])
    antennas = map_antennas(grid)
    antinodes = set()
    for antenna in antennas:
        for i, pos1 in enumerate(antennas[antenna]):
            for j, pos2 in enumerate(antennas[antenna][i + 1:]):
                antinodes.add((pos1[0], pos1[1]))
                antinodes.add((pos2[0], pos2[1]))
                di, dj = abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])
                a1i = pos1[0] + di if pos1[0] > pos2[0] else pos1[0] - di
                a1j = pos1[1] + dj if pos1[1] > pos2[1] else pos1[1] - dj
                while is_valid_coord(a1i, a1j, n, m):
                    antinodes.add((a1i, a1j))
                    a1i = a1i + di if pos1[0] > pos2[0] else a1i - di
                    a1j = a1j + dj if pos1[1] > pos2[1] else a1j - dj

                a2i = pos2[0] + di if pos1[0] < pos2[0] else pos2[0] - di
                a2j = pos2[1] + dj if pos1[1] < pos2[1] else pos2[1] - dj
                while is_valid_coord(a2i, a2j, n, m):
                    antinodes.add((a2i, a2j))
                    a2i = a2i + di if pos1[0] < pos2[0] else a2i - di
                    a2j = a2j + dj if pos1[1] < pos2[1] else a2j - dj

    return len(antinodes)


def is_valid_coord(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


if __name__ == '__main__':
    print(count_antinodes())