
def romanToInt(s: str) -> int:
    c_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman_int = 0
    for i, c in enumerate(s):
        val = c_to_int[c]
        if i + 1 < len(s) and c_to_int[c] < c_to_int[s[i + 1]]:
            val *= -1
        roman_int += val

    return roman_int
