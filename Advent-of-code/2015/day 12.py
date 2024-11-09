
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


def main():
    with (open('input.txt') as f):
        lines = f.readlines()
        print(find_all_numbers(lines[0]))


if __name__ == '__main__':
    main()
