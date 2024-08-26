
def remove_digit(number: str, digit: str) -> str:
    max_number = 0
    for i in range(len(number)):
        if number[i] == digit:
            cur = number[:i] + number[i + 1:]
            if int(cur) > max_number:
                max_number = int(cur)
    return str(max_number)
