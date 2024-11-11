import json


def find_all_numbers(text):
    num_sum = 0
    digits = ''

    for i,c in enumerate(text):
        if i > 0 and not c.isdigit() and text[i-1].isdigit():
            num = int(digits)
            num_sum += num
            digits = ''
        elif c == "-":
            if digits:
                num = int(digits)
                num_sum += num
                digits = ''
            digits += '-'
        elif c.isdigit():
            digits += c
    return num_sum


def count_in_json(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, str) and data.isdigit():
        return int(data)
    elif isinstance(data, dict) and ('red' not in data.values()) and ('red' not in data.keys()):
        return sum(count_in_json(value) for value in data.values())
    elif isinstance(data, list):
        return sum([count_in_json(value) for value in data])
    return 0


def main():
    with (open('input.txt') as f):
        json_string = f.read().strip()
        js = json.loads(json_string)
        print(count_in_json(js))


if __name__ == '__main__':
    main()
