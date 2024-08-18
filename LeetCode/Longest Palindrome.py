
def longest_palindrome(s: str) -> int:
    letters_count = count_letters(s)
    even_count = []
    odd_count = 0
    for letter in letters_count:
        even_count.append([letter, letters_count[letter] // 2])
        if letters_count[letter] % 2 != 0:
            odd_count = 1
    return len(''.join([letter * count for letter, count in even_count])) * 2 + odd_count


def count_letters(s):
    letters_count = {}
    for c in s:
        letters_count[c] = letters_count.get(c, 0) + 1
    return letters_count
