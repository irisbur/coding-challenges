from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    stack = [(sr, sc)]
    start_color = image[sr][sc]

    if start_color == color:
        return image

    while stack:
        curr_idx = stack.pop()

        if image[curr_idx[0]][curr_idx[1]] == start_color:
            image[curr_idx[0]][curr_idx[1]] = color

            for direction in directions:
                i, j = curr_idx[0] + direction[0], curr_idx[1] + direction[1]
                if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == start_color:
                    stack.append((i, j))

    return image

