def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    l = 0
    letter_set = {}

    for r in range(len(s)):
        if s[r] in letter_set and letter_set[s[r]] >= l:
            l = letter_set[s[r]] + 1

        letter_set[s[r]] = r
        max_len = max(max_len, r - l + 1)

    return max_len


print(lengthOfLongestSubstring("tmmzuxt"))
