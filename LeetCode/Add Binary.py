
def add_binary(a: str, b: str) -> str:
    carry = 0
    n, m = len(a) - 1, len(b) - 1
    num_string = ''

    while n >= 0 or m >= 0 or carry != 0:
        d1 = int(a[n]) if n >= 0 else 0
        d2 = int(b[m]) if m >= 0 else 0

        total = d1 + d2 + carry
        num_string = str(total % 2) + num_string
        carry = total // 2
        n -= 1
        m -= 1
    return num_string

print(add_binary("11", "1"))