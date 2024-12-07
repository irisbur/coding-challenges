import re


def parse_input():
    with (open('input.txt') as f):
        input_string = ''.join(f.readlines())
        return input_string

def find_operations(text):
    pattern = "mul\([0-9]*,[0-9]*\)"
    mul_regex = re.compile(pattern)
    return mul_regex.findall(text)


def result_of_mult(lines):
    total = 0
    for line in lines:
        line = line[4:-1].split(',')
        n1, n2 = int(line[0]), int(line[1])
        total += n1 * n2
    return total

def start_from_do(input_string):
    index = input_string.find("do")
    if index != -1:
        return input_string[index:]
    else:
        return ""

def find_do_operations(text):
    operations = []
    splitted = text.split("don't")
    operations.extend(find_operations(splitted[0]))
    for part in splitted[1:]:
        part = start_from_do(part)
        operations.extend(find_operations(part))
    return operations


if __name__ == '__main__':
    input_string = parse_input()
    operations = find_do_operations(input_string)
    print(result_of_mult(operations))
