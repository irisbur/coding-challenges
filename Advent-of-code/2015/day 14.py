

def calculate_distance(v_fly, t_fly, t_rest, total_t):
    round_time = t_fly + t_rest
    rounds = (total_t // round_time)
    distance_in_round = v_fly * t_fly
    distance = rounds * distance_in_round
    rem = total_t % round_time
    if rem > 0:
        distance += min(rem, t_fly) * v_fly
    return distance


def argmax(dists):
    best = max(dists)
    return [i for i, d in enumerate(dists) if d == best]


def calculate_points(deer, total_time):
    deer_points = [0] * len(deer.keys())
    deer_dists = [0] * len(deer.keys())
    for t in range(1, total_time+1):
        for i, c_deer in enumerate(deer):
            v_fly, t_fly, t_rest = deer[c_deer]
            dist = calculate_distance(v_fly, t_fly, t_rest, t)
            deer_dists[i] = dist
        indices = argmax(deer_dists)
        for j in indices:
            deer_points[j] += 1
    print(max(deer_points))


def main():
    with (open('input.txt') as f):
        lines = f.readlines()
        deer = dict()
        for line in lines:
            line = line.split()
            name = line[0]
            deer[name] = (int(line[3]), int(line[6]), int(line[-2]))
        calculate_points(deer, 2503)


if __name__ == '__main__':
    main()

