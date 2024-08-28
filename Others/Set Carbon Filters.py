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



