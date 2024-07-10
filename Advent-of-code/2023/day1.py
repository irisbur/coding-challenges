
import re

text_to_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def calibration_sum(in_lines):
    calibration_sum = 0
    for line in in_lines:
        num1 = re.search(r'(\d)', line).group()
        num2 = re.search(r'(\d)', line[:-1][::-1]).group()
        calibration_sum += int(num1)*10 + int(num2[::-1])
    return calibration_sum


def sol1(in_lines):
    calibration_sum = 0
    for line in in_lines:
        matches_to_indices = {}
        for num in text_to_num:
            match = re.search(r'' + num, line)
            if match:
                matches_to_indices[num] = match.start()
        match_first_digit = re.search(r'(\d)', line)
        if match_first_digit:
            matches_to_indices[match_first_digit.group()] = match_first_digit.start()
        match_last_digit = re.search(r'(\d)', line[:-1][::-1])
        if match_last_digit:
            matches_to_indices[match_last_digit.group()] = len(line[:-1][::-1]) - 1 - match_last_digit.start()

        indices_to_match = {v: k for k, v in matches_to_indices.items()}
        min_num = indices_to_match[min(indices_to_match)]
        max_num = indices_to_match[max(indices_to_match)]
        first_digit = int(min_num) if min_num.isdigit() else text_to_num[min_num]
        second_digit = int(max_num) if max_num.isdigit() else text_to_num[max_num]
        calibration_sum += int(first_digit) * 10 + int(second_digit)
    return calibration_sum


def main():
    with open('in1_23.txt') as f:
        lines = f.readlines()
        print(sol1(lines))


if __name__ == '__main__':
    main()

