import re


def parse_input():
    with (open('input.txt') as f):
        text_list = f.readlines()
        return text_list

def find_operations(text_list):
    pattern = "mul\([0-9]*,[0-9]*\)"
    mul_regex = re.compile(pattern)
    operations = []
    for text in text_list:
        operations.extend(mul_regex.findall(text))
    return operations


def result_of_mult(lines):
    total = 0
    for line in lines:
        line = line[4:-1].split(',')
        n1, n2 = int(line[0]), int(line[1])
        total += n1 * n2
    return total


if __name__ == '__main__':
    text_list = parse_input()
    operations = find_operations(text_list)
    print(result_of_mult(operations))
