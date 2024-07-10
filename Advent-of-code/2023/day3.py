
def is_symbol(char):
    if char != '.' and not char.isdigit() and not char.isalpha():
        return True


def is_adjacent_symbol(input_matrix, i, j):
    if i > 0 and is_symbol(input_matrix[i - 1][j]):
        return True
    if i < len(input_matrix) - 1 and is_symbol(input_matrix[i + 1][j]):
        return True
    if j > 0 and is_symbol(input_matrix[i][j - 1]):
        return True
    if j < len(input_matrix[i]) - 1 and is_symbol(input_matrix[i][j + 1]):
        return True
    if i > 0 and j > 0 and is_symbol(input_matrix[i - 1][j - 1]):
        return True
    if i < len(input_matrix) - 1 and j < len(input_matrix[i]) - 1 and is_symbol(input_matrix[i + 1][j + 1]):
        return True
    if i > 0 and j < len(input_matrix[i]) - 1 and is_symbol(input_matrix[i - 1][j + 1]):
        return True
    if i < len(input_matrix) - 1 and j > 0 and is_symbol(input_matrix[i + 1][j - 1]):
        return True
    return False


def sum_part_numbers(input_matrix):
    parts_sum = 0
    for i in range(len(input_matrix)):
        current_number = ''
        is_current_number_adjacent_to_symbol = False
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j].isdigit():
                # check value adjacent is a symbol but not a dot, not this is a matrix
                current_number += input_matrix[i][j]
                if is_adjacent_symbol(input_matrix, i, j):
                    is_current_number_adjacent_to_symbol = True
            else:
                if is_current_number_adjacent_to_symbol:
                    parts_sum += int(current_number)
                current_number = ''
                is_current_number_adjacent_to_symbol = False
        if is_current_number_adjacent_to_symbol:
            parts_sum += int(current_number)
    return parts_sum


def adjacent_star_index(input_matrix, i, j):
    adjacent_stars = []
    if i > 0 and input_matrix[i - 1][j] == '*':
        adjacent_stars.append((i-1, j))
    if i < len(input_matrix) - 1 and input_matrix[i + 1][j] == '*':
        adjacent_stars.append((i+1, j))
    if j > 0 and input_matrix[i][j - 1] == '*':
        adjacent_stars.append((i, j-1))
    if j < len(input_matrix[i]) - 1 and input_matrix[i][j + 1] == '*':
        adjacent_stars.append((i, j+1))
    if i > 0 and j > 0 and input_matrix[i - 1][j - 1] == '*':
        adjacent_stars.append((i-1, j-1))
    if i < len(input_matrix) - 1 and j < len(input_matrix[i]) - 1 and input_matrix[i + 1][j + 1] == '*':
        adjacent_stars.append((i+1, j+1))
    if i > 0 and j < len(input_matrix[i]) - 1 and input_matrix[i - 1][j + 1] == '*':
        adjacent_stars.append((i-1, j+1))
    if i < len(input_matrix) - 1 and j > 0 and input_matrix[i + 1][j - 1] == '*':
        adjacent_stars.append((i+1, j-1))
    return adjacent_stars


def count_gear_ratio(input_matrix):
    total_gear_ratio = 0
    numbers_star_dict = {}
    for i in range(len(input_matrix)):
        current_number = ''
        current_adjacent_star_index = []
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j].isdigit():
                current_number += input_matrix[i][j]
                current_adjacent_star_index += adjacent_star_index(input_matrix, i, j)
            else:
                if len(current_adjacent_star_index) > 0:
                    numbers_star_dict[current_number] = current_adjacent_star_index
                current_number = ''
                current_adjacent_star_index = []

    stars_index_to_count_dict = {}
    for number, stars_indices in numbers_star_dict.items():
        stars_indices = list(set(stars_indices))
        for star_index in stars_indices:
            if star_index in stars_index_to_count_dict:
                stars_index_to_count_dict[star_index].append(number)
            else:
                stars_index_to_count_dict[star_index] = [number]

    for star_index, numbers in stars_index_to_count_dict.items():
        gear_ratio = 1
        if len(numbers) == 2:
            for number in numbers:
                gear_ratio *= int(number)
            total_gear_ratio += gear_ratio
    return total_gear_ratio


def adjacent_stars(input_matrix, i, j):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    stars = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(input_matrix) and 0 <= nj < len(input_matrix[0]):
            if input_matrix[ni][nj] == '*':
                stars.append((ni, nj))
    return stars


def count_gear_ratio1(input_matrix):
    total_gear_ratio = 0
    stars_to_numbers = {}

    for i in range(len(input_matrix)):
        j = 0
        while j < len(input_matrix[i]):
            if input_matrix[i][j].isdigit():
                num_start = j
                while j < len(input_matrix[i]) and input_matrix[i][j].isdigit():
                    j += 1
                number = int(''.join(input_matrix[i])[num_start:j])
                # Get stars adjacent to the entire number
                for k in range(num_start, j):
                    for star in adjacent_stars(input_matrix, i, k):
                        if star not in stars_to_numbers:
                            stars_to_numbers[star] = []
                        stars_to_numbers[star].append(number)
            j += 1

    for numbers in stars_to_numbers.values():
        unique_numbers = list(set(numbers))
        if len(unique_numbers) == 2:
            gear_ratio = unique_numbers[0] * unique_numbers[1]
            total_gear_ratio += gear_ratio

    return total_gear_ratio


def main():
    with open('input3_23.txt') as f:
        input_matrix = []
        for line in f:
            input_matrix.append(list(line[:-1]))
        print(count_gear_ratio1(input_matrix))


if __name__ == '__main__':
    main()

