

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
        return ['0', '1', '2']
    ops = generate_op_combinations(n-1)
    new = []
    for comb in ops:
        new.append("0" + comb)
        new.append("1" + comb)
        new.append("2" + comb)
    return new

def concat(a,b):
    return int(str(a) + str(b))

def is_calibrated_(result, numbers, combination):
    return calibration_result(numbers, combination) == result

def calibration_result(numbers, combination):
    total = numbers[0]
    for i, c in enumerate(combination):
        if c == '0':
            total += numbers[i+1]
        elif c == '1':
            total *= numbers[i+1]
        elif c == '2':
            total = concat(total, numbers[i+1])
    return total


def total_calibration_result(equations):
    total = 0
    for equation in equations:
        result, numbers = equation
        combinations = generate_op_combinations(len(numbers) - 1)
        for combination in combinations:
            is_calibrated = is_calibrated_(result, numbers, combination)
            if is_calibrated != 0:
                # print(equation, combination)
                total += result
                break
    return total


if __name__ == '__main__':
    equations = parse_input()
    print(total_calibration_result(equations))

