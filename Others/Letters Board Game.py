# Task 1
#
# A game board has a row of N+1 fields, numbered from 0 to N from left to right.
# One letter ("a" or "b") is written between every two adjacent fields.
# Letters on the board are described by a string L of length N, where L[K] (for K within the range [0..N-1])
# is the letter between fields K and K+1.
# For example, given L = "aaabab" and N = 6 the game board at the beginning will look like this:
#  a a a b a b
# 0 1 2 3 4 5 6
#
# There is a game piece standing on some field on the board. It can move one field to the left or to the right,
# passing over one of the letters. The letter over which the game piece passes switches to the opposite one
# ("a" becomes "b" and "b" becomes "a"). The game piece can move multiple times, so letters may also be switched
# multiple times.
# For above example, if the game piece stood on the field number 3 and then moved to the left, the game board would
# look like the picture below:
#  a a aXb a b      a aXb b a b
# 0 1 2 3 4 5 6 -> 0 1 2 3 4 5 6
#
#
# The game piece initially stands on a field designated as the start.
# What is the minimum number of moves after which there will be the same number of letters "a" and "b" on the board?
# If it is impossible to achieve such a situation, return -1.
#
# Write a function:
# class Solution { public int solution(String L, int start); }
#
# that, given a string L of length N and an integer start, returns the minimum number of moves such that,
# after those moves, there will be the same number of letters "a" and "b" on the board (or returns -1 if
# it is impossible).
#
#
# Examples:
# 1. For L = "aaabab", start = 0, the game piece must move one field to the right.
# This way, the first letter of L will be switched to produce string "baabab".
# Both letters occur in this string three times. The function should return 1.
# 2. For L = "aaabab", start = 6, the game piece has to move five times to the left:
# "aaabab"
# "aaabaa" → "aaabba" → "aaaaba" → "aababa" → "abbaba"
# The function should return 5.
# 3. For L = "ababa", start = 1, it is impossible to equalize the number of letters "a" and "b".
# The function should return -1.
# 4. For L = "babbaa", start = 2, the number of letters "a" and "b" is already equal. The function should return 0.
# Assume that:
# • N is an integer within the range [1..100];
# • string L is made only of the characters 'a' and/or 'b';
# start is an integer within the range [0..N].
# In your solution, focus on correctness.
# The performance of your solution will not be the focus of the assessment.


def solution(L, start):
    n = len(L)
    if n % 2 == 1:
        return -1

    cntr = {'a': 0, 'b': 0}

    for i in range(n):
        cntr[L[i]] = cntr[L[i]] + 1

    if cntr['a'] == cntr['b']:
        return 0

    s_list = list(L)
    steps = 0
    move_direction = 1
    current = start
    if start == n:
        move_direction = -1
        current = n - 1
    while cntr['a'] != cntr['b'] and steps < 4 * n:
        steps += 1
        if s_list[current] == 'a':
            cntr['a'] = cntr['a'] - 1
            cntr['b'] = cntr['b'] + 1
            s_list[current] = 'b'
        else:
            cntr['a'] = cntr['a'] + 1
            cntr['b'] = cntr['b'] - 1
            s_list[current] = 'a'

        current = current + move_direction

        if current >= n:
            move_direction = -1
            current = n - 1
        elif current <= -1:
            move_direction = 1
            current = 0


    if cntr['a'] == cntr['b']:
        return steps
    return -1

print(solution('aaabab', 0))
print(solution('aaabab', 6))
print(solution('ababa', 1))
print(solution('babbaa', 2))
print(solution('aaaa', 4))
print(solution('aaaaba', 4))
