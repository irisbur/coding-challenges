
def add_binary(a: str, b: str) -> str:
    c = '0'
    sum_string = ''
    n, m = len(a) - 1, len(b) - 1
    while n >= 0 and m >= 0:
        r, c = sum_with_carry(a[n], b[m], c)
        sum_string = r + sum_string
        n -= 1
        m -= 1

    while n >= 0:
        r, c = sum_with_carry(a[n], c, '0')
        sum_string = r + sum_string
        n -= 1

    while m >= 0:
        r, c = sum_with_carry(b[m], c, '0')
        sum_string = r + sum_string
        m -= 1

    if c == '1':
        sum_string = c + sum_string
    return sum_string


def sum_with_carry(a, b, c):
    if a == '0' and b == '0' and c == '0':
        return '0', '0'
    if (a == '1' and b == '0' and c == '0') or (a == '0' and b == '1' and c == '0') or (
            a == '0' and b == '0' and c == '1'):
        return '1', '0'
    if (a == '1' and b == '1' and c == '0') or (a == '0' and b == '1' and c == '1') or (
            a == '1' and b == '0' and c == '1'):
        return '0', '1'
    elif a == '1' and b == '1' and c == '1':
        return '1', '1'
    return -1, -1