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


def count_in_list(json_list):
    count = 0
    for v in json_list:
        if isinstance(v, dict):
            count += count_in_dict(v)
        elif isinstance(v, list):
            count += count_in_list(v)
        elif isinstance(v, int):
            count += v
        elif v.isdigit():
            count += int(v)
    return count


def count_in_dict(json_dict):
    count = 0
    for k, v in json_dict.items():
        if k == 'red' or v == 'red':
            return 0
        elif isinstance(v, dict):
            count += count_in_dict(v)
        elif isinstance(v, list):
            count += count_in_list(v)
        elif isinstance(v, int):
            count += v
        elif v.isdigit():
            count += int(v)
    return count


def count_in_json(input_json):
    count = 0
    if isinstance(input_json, dict):
        count += count_in_dict(input_json)
    elif isinstance(input_json, list):
        count += count_in_list(input_json)
    return count


def main():
    with (open('input.txt') as f):
        json_string = f.readlines()[0]
        js = json.loads(json_string)

        print(count_in_json(js))


if __name__ == '__main__':
    main()
