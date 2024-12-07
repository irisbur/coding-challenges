

def parse_input():
    with (open('input.txt') as f):
        lines = f.readlines()
        equations = []
        for line in lines:
            line = line.split(':')
            result, numbers = int(line[0]), [int(n) for n in line[1].split()]
            equations.append([result, numbers])
        return equations


def generate_op_combinations(n):
    if n == 1:
        return ['0', '1']
    ops = generate_op_combinations(n-1)
    new = []
    for comb in ops:
        new.append("0" + comb)
        new.append("1" + comb)
    return new


def calibration_result(equation):
    result, numbers = equation
    combinations = generate_op_combinations(len(numbers) - 1)
    for combination in combinations:
        total = numbers[0]
        for i, c in enumerate(combination):
            if c == '0':
                total += numbers[i+1]
            else:
                total *= numbers[i+1]
        if total == result:
            return result
    return 0


def total_calibration_result(equations):
    total = 0
    for equation in equations:
        total += calibration_result(equation)
    return total


if __name__ == '__main__':
    equations = parse_input()
    print(total_calibration_result(equations))

