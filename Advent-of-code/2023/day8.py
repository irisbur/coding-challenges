# Part 1 #

# Algorithm:
# parse all the names into a dictionary from key to (l,r) tuple and iterate starting from 'AAA'
# through the steps until we reach 'ZZZ', increment the steps count, choose between l and r using the
# step in sides mod len(sides).
# if we have n names creating the dictionary will take O(n) space and time, iterating will take O(l)
# where l is the number of steps.
def count_steps():
    with (open("input.txt", "r") as input_file):
        sides = input_file.readline()[:-1]
        side_to_idx = {'L': 0, 'R': 1}
        step_to_next = parse_input_to_dict(input_file.readlines())

        steps = 0
        current_step = 'AAA'
        while current_step != 'ZZZ':
            side = side_to_idx[sides[steps % len(sides)]]
            current_step = step_to_next[current_step][side]
            steps += 1

    print(steps)


def parse_input_to_dict(lines):
    step_to_next = {}
    for line in lines[1:]:
        current_step = line.split('=')[0][:-1]
        left, right = line.split('= (')[1][:3], line.split(', ')[1][:-2]
        step_to_next[current_step] = (left, right)
    return step_to_next


# Part 2 #

# At the beginning I tried to wait until all the initial values will have 'Z', but after this solution took too long
# I realized that it's enough to find the minimal value of each initial step and then find the lowest common multiple
# (LCM), that is also the multiple of initial values divided by the greatest common divisor (GCD).
# so now the question is, how to find the GCD? I'll implement the Euclidean algorithm.
def count_steps_multiple_starts():
    with (open("input.txt", "r") as input_file):
        sides = input_file.readline()[:-1]
        side_to_idx = {'L': 0, 'R': 1}
        step_to_next = parse_input_to_dict(input_file.readlines())

        steps = 0
        current_steps = [step_name for step_name in step_to_next if step_name[2] == 'A']
        smallest_steps_for_path = [0] * len(current_steps)
        while 0 in smallest_steps_for_path:
            side = side_to_idx[sides[steps % len(sides)]]
            for i in range(len(current_steps)):
                current_steps[i] = step_to_next[current_steps[i]][side]
                if current_steps[i][2] == 'Z' and smallest_steps_for_path[i] == 0:
                    smallest_steps_for_path[i] = steps + 1
            steps += 1

        curr_lcm = smallest_steps_for_path[0]
        for i in range(1, len(smallest_steps_for_path)):
            curr_lcm = lcm(curr_lcm, smallest_steps_for_path[i])
    print(curr_lcm)


def lcm(a, b):
    return int(a / gcd(a, b) * b)


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


if __name__ == "__main__":
    count_steps_multiple_starts()
