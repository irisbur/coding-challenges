from collections import Counter


def parse_input():
    with (open('input.txt') as f):
        lines = f.readlines()
        left, right = [], []
        for line in lines:
            line = [l.strip() for l in line.split()]

            left.append(int(line[0]))
            right.append(int(line[1]))
        return left, right

def part_1():
    left, right = parse_input()
    left.sort()
    right.sort()

    distances = 0
    for i in range(len(left)):
        distances += abs(left[i] - right[i])
    return distances

def part_2():
    left, right = parse_input()
    count_r = Counter(right)
    similarity = 0

    for n in left:
        if n in count_r:
            similarity += n * count_r[n]

    return similarity


if __name__ == '__main__':
    print(part_2())
