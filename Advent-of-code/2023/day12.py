

def count_sum_arrangements():
    with open("input.txt", "r") as input_file:
        rows = [line.split() for line in input_file.readlines()]
        sum_arrangements = 0

        for row in rows:
            row_count = count_arrangements(row)
            sum_arrangements += row_count

        return sum_arrangements


def count_arrangements(row):
    spring_list, num_list = list(row[0]), [int(n) for n in row[1].split(',')]
    return recursive_count(spring_list, num_list)


def recursive_count(spring_list, num_list):
    if '?' not in spring_list:
        return 1 if is_spring_list_valid(spring_list, num_list) else 0

    q_i = spring_list.index('?')
    switch_with_valid = list(''.join(spring_list[:q_i]) + '.' + ''.join(spring_list[q_i + 1:]))
    switch_with_damaged = list(''.join(spring_list[:q_i]) + '#' + ''.join(spring_list[q_i + 1:]))
    return recursive_count(switch_with_valid, num_list) + recursive_count(switch_with_damaged, num_list)


def is_spring_list_valid(spring_list, num_list):
    if not num_list:
        return '#' not in spring_list

    contiguous_springs = 0
    spring_group = -1
    for i, c in enumerate(spring_list):
        if spring_group > len(num_list):
            return False

        if c == '#':
            if i > 0 and spring_list[i-1] != '#' or i == 0:
                spring_group += 1
                contiguous_springs = 0
            contiguous_springs += 1
            if spring_group < len(num_list) and contiguous_springs > num_list[spring_group]:
                return False
        if c == '.':
            if i > 0 and spring_list[i-1] == '#':
                if spring_group < len(num_list) and contiguous_springs < num_list[spring_group]:
                    return False

    return spring_group == (len(num_list) - 1) and contiguous_springs == num_list[-1]


print(count_sum_arrangements())
