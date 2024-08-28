# Task 2
#
# There are N houses along the street. Carbon filters are already installed in some of them.
# We would like to install filters in the remaining houses (those that do not possess them yet).
# Two types of filter, named 'a' and 'b', are being used. The filters work best if no three adjacent houses have the
# same type of filter. The houses are represented as a string of characters 'a', 'b' and '?'
# ('a' and 'b' denote a house with a filter of a given type installed; '?' represents a house with no filter yet).
# Your task is to make a plan of the filter types to be installed in the houses that do not yet have them.
#
# Write a function
# class Solution { public String solution (String S);}
#
# that, given a string S of length N, returns a string that is the result of replacing each '?' in string S with an
# 'a' or a 'b' character and does not contain three identical consecutive letters (in other words, neither
# "aaa" nor "bbb" may occur in the processed string).

# Examples:
# 1. Given S = "a?bb", your function should return "aabb".
# 2. Given S = "??abb", your function should return "ababb", "bbabb" or "baabb".
# 3. Given S = "a?b?aa", your function should return "aabbaa".
# 4. Given S = "aa??aa", your function should return "aabbaa".
#
# Write an efficient algorithm for the following assumptions:
# string S is made only of the following characters: 'a', 'b' and/or '?'; • N is an integer within the range
# [1..500,000];
# * it is always possible to create a plan so that there are no three identical consecutive filters.


def solution(S):
    n = len(S)
    if n == 1:
        return 'a' if S == '?' else S

    question_marks = find_question_maks(S)
    S_options = [S]
    while question_marks:
        i = question_marks.pop()
        new_options = []
        for s in S_options:
            s_a = s[:i] + 'a' + s[i + 1:]
            if is_s_still_valid(s_a, i):
                new_options.append(s_a)

            s_b = s[:i] + 'b' + s[i + 1:]
            if is_s_still_valid(s_b, i):
                new_options.append(s_b)
        S_options = new_options
    return S_options[0]


def is_s_still_valid(s, i):
    n = len(s)
    if i == 0:
        cntr = {}
        for i in range(3):
            cntr[s[i]] = cntr.get(s[i], 0) + 1
        return len(cntr) > 1
    elif i == (n - 1):
        cntr = {}
        for i in range(n - 3, n):
            cntr[s[i]] = cntr.get(s[i], 0) + 1
        return len(cntr) > 1
    elif s[i] == s[i - 1] and s[i] == s[i + 1]:
        return False
    elif is_valid_index(i - 2, n) and s[i - 1] == s[i - 2] and s[i - 1] == s[i]:
        return False
    elif is_valid_index(i + 2, n) and s[i + 1] == s[i + 2] and s[i + 1] == s[i]:
        return False
    return True


def find_question_maks(S):
    question_marks = []
    for i in range(len(S)):
        if S[i] == '?':
            question_marks.append(i)
    return question_marks


def is_valid_index(i, n):
    return 0 <= i < n


