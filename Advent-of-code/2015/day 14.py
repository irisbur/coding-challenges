

def calculate_distance(v_fly, t_fly, t_rest, total_t):
    round_time = t_fly + t_rest
    rounds = (total_t // round_time)
    distance_in_round = v_fly * t_fly
    distance = rounds * distance_in_round
    rem = total_t % round_time
    if rem > 0:
        distance += min(rem, t_fly) * v_fly
    return distance


def main():
    with (open('input.txt') as f):
        lines = f.readlines()
        win_dist = 0
        for line in lines:
            line = line.split()
            v_fly, t_fly, t_rest = int(line[3]), int(line[6]), int(line[-2])
            d = calculate_distance(v_fly, t_fly, t_rest, 2503)
            print(d)
            win_dist = max(win_dist, d)

        print(win_dist)


if __name__ == '__main__':
    main()

