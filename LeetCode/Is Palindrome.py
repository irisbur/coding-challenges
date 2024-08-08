from collections import Counter


# Solution runs in O(n) time and O(1) space.
def is_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True


# Solution that takes advantage of pythonic ways
def is_pal(s: str) -> bool:
    clean = ''.join([c.lower() for c in s if c.isalnum()])
    return clean == clean[::-1]


def is_anagram(s, t):
    # runtime O(n+m).
    return Counter(s) == Counter(t)
    # another solution is sorted(s) == sorted(t) but this is O(nlogn + mlogm).


