# There is a board made of two rows and N columns. The board is represented by two strings, row1 and row2,
# made of characters 'R, W and/or '?'. A board is balanced if, in each row and in each column, the number of
# characters R' is equal to the number of characters 'W’. For example, the following board is balanced:
#
# ?RW?WR
# ?WR?RW
#
# and the following board is not balanced:
#
# W?WR?
# R??W?
#
# (there are two characters 'W' and one character 'R' in the first row).
# The question marks (‘?') can be replaced with 'W’ or 'R'.
# What is the minimum number of replacements needed to balance the board?

# W?WR?
# R??W?

# Write a function:
# def solution(row1, row2):
#     pass
# that, given two strings row and row made of N characters each, returns the minimum number of replacements needed to
# balance the board. If it is not possible to balance the board, the function should return -1.
from collections import Counter


def balance_board(row1, row2):
    n = len(row1)
    counter1, counter2 = Counter(row1),  Counter(row2)

    steps = 0

    for i in range(n):
        if row1[i] == row2[i] and row1[i] != '?':
            return -1

    return steps

