import re


def is_game_possible(game_description):
    max_in_color = {'red': 12, 'green': 13, 'blue': 14}
    game_by_order, numbers = create_game_dict(game_description)
    for i, color in enumerate(game_by_order):
        if int(numbers[i]) > max_in_color[color[0]]:
            return False
    return True


def create_game_dict(game_description):
    game_dict = {}
    numbers = re.findall(r'\d+', game_description)
    red_ind = game_description.find(r'red')
    if red_ind != -1:
        game_dict['red'] = red_ind
    green_ind = game_description.find('green')
    if green_ind != -1:
        game_dict['green'] = green_ind
    blue_ind = game_description.find('blue')
    if blue_ind != -1:
        game_dict['blue'] = blue_ind
    game_by_order = sorted(game_dict.items(), key=lambda x: x[1])
    return game_by_order, numbers


def sol2a(in_lines):
    ids_sum = 0
    for line in in_lines:
        match = re.search(r'\d+', line)
        game_number = int(match.group())
        line = line[:match.end()] + ";" + line[match.end():]
        game_descriptions = line[6:-1].split(';')[1:]
        for game_description in game_descriptions:
            if not is_game_possible(game_description):
                game_number = 0
                break
        ids_sum += game_number
    return ids_sum


def calc_cube_power(game_descriptions):
    red_list, green_list, blue_list = [], [], []
    for game_description in game_descriptions:
        game_by_order, numbers = create_game_dict(game_description)
        for i, color in enumerate(game_by_order):
            if color[0] == 'red':
                red_list.append(int(numbers[i]))
            if color[0] == 'green':
                green_list.append(int(numbers[i]))
            if color[0] == 'blue':
                blue_list.append(int(numbers[i]))
    pow = 1
    if len(red_list) > 0:
        pow *= max(red_list)
    if len(green_list) > 0:
        pow *= max(green_list)
    if len(blue_list) > 0:
        pow *= max(blue_list)
    print(pow)
    return pow


def sol2b(in_lines):
    pow_sum = 0
    for line in in_lines:
        match = re.search(r'\d+', line)
        line = ";" + line[match.end():]
        game_descriptions = line.split(';')[1:]
        game_pow = calc_cube_power(game_descriptions)
        pow_sum += game_pow
    return pow_sum


def main():
    with open('in2_23.txt') as f:
        lines = f.readlines()
        print(sol2b(lines))


if __name__ == '__main__':
    main()
