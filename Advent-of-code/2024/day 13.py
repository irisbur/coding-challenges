import numpy as np
from numpy.linalg import LinAlgError, solve


def parse_file_lines(file_lines):
    matrices = []
    vectors = []
    block = []

    for line in file_lines:
        stripped_line = line.strip()
        if stripped_line:
            block.append(stripped_line)
        else:
            if block:
                matrix, vector = parse_block(block)
                matrices.append(matrix)
                vectors.append(vector)
                block = []
    return matrices, vectors

def parse_block(block):
    matrix = []
    vector = []

    for line in block:
        if line.startswith("Button"):
            parts = line.split(":")[1].strip().split(",")
            row = []
            for part in parts:
                _, value = part.split("+")
                row.append(float(value.strip()))
            matrix.append(row)
        elif line.startswith("Prize"):
            parts = line.split(":")[1].strip().split(",")
            for part in parts:
                _, value = part.split("=")
                vector.append(float(value.strip()))

    return np.array(matrix).T, np.array(vector) + 10000000000000

def solve_presses(buttons_matrix, prize):
    try:
        presses = solve(buttons_matrix, prize)
        if not np.isclose(presses - np.round(presses),np.array([0,0]), atol=1e-4).all():
            return 0

        cost = 3 * presses[0] + presses[1]
        return cost
    except LinAlgError as e:
        print("Matrix inversion failed or system unsolvable:", e)
        return 0


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    matrices, vectors = parse_file_lines(file_lines)
    total_cost = 0

    for idx, (matrix, vector) in enumerate(zip(matrices, vectors), start=1):
        total_cost += solve_presses(matrix, vector)
    print(total_cost)