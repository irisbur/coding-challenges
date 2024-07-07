# Part 1 #

def translate_seeds_to_locations(seeds_map, dest, source, range_length):
    for seed in seeds_map:
        if source <= seed < (source + range_length):
            seeds_map[seed] = dest + (seed - source)


def print_lowest_location_number():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        seeds = lines[0].split(":")[1].split()
        seeds_map = {int(seed): int(seed) for seed in seeds}
        seeds_map = update_seeds_locations(lines, seeds_map)
    print(min(seeds_map.values()))


# Part 2 #
# The code below is too naive, fails on large input.

def update_seeds_locations(lines, seeds_map):
    for line in lines[3:-1]:
        if line == '\n' or line[0].isalpha():
            new_seeds_map = {int(seed): int(seed) for seed in seeds_map.values()}
            seeds_map = new_seeds_map
            continue
        values_list = line.split()
        rule = list(map(int, values_list))
        translate_seeds_to_locations(seeds_map, rule[0], rule[1], rule[2])
    return seeds_map


def print_lowest_location_number_with_range():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        seeds_and_ranges = list(map(int, lines[0].split(":")[1].split()))
        seeds_map = {int(i): int(i) for i in range(seeds_and_ranges[0], seeds_and_ranges[0] + seeds_and_ranges[1])}
        seeds_map.update({int(i): int(i) for i in range(seeds_and_ranges[2], seeds_and_ranges[2] + seeds_and_ranges[3])})
        seeds_map = update_seeds_locations(lines, seeds_map)

    print(min(seeds_map.values()))


if __name__ == "__main__":
    print_lowest_location_number_with_range()
