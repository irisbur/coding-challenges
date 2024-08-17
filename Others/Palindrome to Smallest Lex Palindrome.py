
# Given a symmetric string (a palindrome), modify it to create the smallest
# lexicographically possible palindrome. The output should maintain the palindrome property while being
# as small as possible in lexicographical order.

# e.g yxxy -> xyyx
# ded -> ded


def find_smallest_pal(name_string):
    freqs = count_frequencies(name_string)
    count_arr = [[c, freqs[c] // 2] for c in sorted(freqs) if freqs[c] > 1]
    first_half = create_first_half(count_arr)
    if len(name_string) % 2 == 0:
        sorted_name = first_half + first_half[::-1]
    else:
        middle = name_string[(len(name_string) - 1) // 2]
        sorted_name = first_half + middle + first_half[::-1]
    return sorted_name


def create_first_half(count_arr):
    return ''.join(c * count for c, count in count_arr)


def count_frequencies(name_string):
    freqs = {}
    for c in name_string:
        freqs[c] = freqs.get(c, 0) + 1
    return freqs

print(find_smallest_pal('baaab'))

