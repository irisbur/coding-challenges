import math
from itertools import permutations


def parse_input(lines):
    ppl = []
    happiness_map = dict()

    for line in lines:
        line = line.split()
        if line[0] not in ppl:
            ppl.append(line[0])
        if line[-1][:-1] not in ppl:
            ppl.append(line[-1][:-1])
        score = int(line[3])
        if line[2] == "lose":
            score *= -1
        happiness_map[(line[0], line[-1][:-1])] = score
    return ppl, happiness_map


def calculate_happiness_in_seating(seating, happiness_map):
    n = len(seating)
    score = 0
    for i in range(n):
        if seating[i] != "Iris" and seating[(i+1)%n] != "Iris":
            score += happiness_map[(seating[i], seating[(i+1) % n])]
        if seating[i] != "Iris" and seating[(i - 1) % n] != "Iris":
            score += happiness_map[(seating[i], seating[(i-1) % n])]
    return score


def main():
    with (open('input.txt') as f):
        lines = f.readlines()
        ppl, happiness_map = parse_input(lines)
        ppl.append("Iris")
        perms = permutations(ppl)
        best_score = 0
        for perm in perms:
            score = calculate_happiness_in_seating(perm, happiness_map)
            best_score = max(score, best_score)
        print(best_score)


if __name__ == '__main__':
    main()
