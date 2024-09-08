from collections import deque, Counter


# Question 1 - warm up
# Given an array of integers, find two distinct numbers whose sum is zero and return their indices.
# If there are multiple valid pairs, return any one. If no such pair exists, return None.
# The algorithm should run in O(n) time complexity.
def two_sum(nums):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = -num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None


# Question 2 - Look and Say
# Given a starting number and an integer n, generate the n-th term in the “look-and-say” sequence.
def look_and_say(number, n):
    current_seq = str(number)

    for i in range(n):
        new_seq = []
        count = 1
        prev_d = current_seq[0]

        for d in current_seq[1:]:
            if d == prev_d:
                count += 1
            else:
                new_seq.append(str(count) + prev_d)
                prev_d = d
                count = 1
        new_seq.append(str(count) + prev_d)
        current_seq = ''.join(new_seq)

    return current_seq


# Island map
# Given an n*m grid with different types of cells
# (.: empty, *: flooded, X: rock, S: start, D: destination),
# find the shortest path from S to D while handling flooding cells that expand at every step.
# Return the number of steps or -1 if unreachable.
def count_steps(island_map):
    n, m = len(island_map), len(island_map[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    si, sj = find_initial_position(island_map)
    qe = deque([(si, sj, 0)])
    visited = {(si, sj)}
    flooded = find_initial_flood(island_map)
    last_flooded_step = -1
    while qe:
        ci, cj, step = qe.popleft()

        if step != last_flooded_step:
            flooded = flood(island_map, flooded)
            last_flooded_step = step

        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if is_position_valid(ni, nj, n, m) and island_map[ni][nj] == "D":
                return step + 1
            elif is_position_valid(ni, nj, n, m) and island_map[ni][nj] == "." and (ni, nj) not in visited:
                visited.add((ni, nj))
                qe.append((ni, nj, step + 1))

    return -1


def find_initial_flood(grid):
    flooded = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                flooded.append((i, j))
    return flooded


def flood(grid, flooded):
    new_flood = []
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i, j in flooded:
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if is_position_valid(ni, nj, n, m) and grid[ni][nj] == ".":
                grid[ni][nj] = "*"
                new_flood.append((ni, nj))
    return new_flood


def is_position_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def find_initial_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return i, j
    return -1, -1


# Question 4: poker hands
# Part 1
# Given a string representing a poker hand (5 cards), determine the type of the hand.
# Types include “Four of a Kind”, “Full House”, “Three of a Kind”, “Two Pair”, “Pair”, and “High Card”.
def get_hand_type(hand):
    cntr = Counter(hand)
    counts = sorted(cntr.values())

    if counts == [1, 4]:
        return "Four of a Kind"
    elif counts == [2, 3]:
        return "Full House"
    elif counts == [1, 1, 3]:
        return "Three of a Kind"
    elif counts == [1, 2, 2]:
        return "Two Pair"
    elif counts == [1, 1, 1, 2]:
        return "Pair"
    return "High Card"


# Part 2
# Write a function that receives two poker hands (handA and handB) and compares their strength to
# determine which is stronger. The function should return:
# 	1 if handA is stronger than handB.
# 	-1 if handB is stronger than handA.
# 	0 if both hands have the same strength.
def stronger_card(handA, handB):
    type_to_strength = {"Four of a Kind": 5, "Full House": 4,
                        "Three of a Kind": 3, "Two Pair": 2, "Pair": 1, "High Card": 0}

    card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, 'J': 11, 'Q': 12, 'K': 13}

    type_a = get_hand_type(handA)
    type_b = get_hand_type(handB)

    if type_to_strength[type_a] > type_to_strength[type_b]:
        return 1
    elif type_to_strength[type_a] < type_to_strength[type_b]:
        return -1
    else:
        sorted_a = sorted(handA, key=lambda x: card_order[x], reverse=True)
        sorted_b = sorted(handB, key=lambda x: card_order[x], reverse=True)

        for i in range(len(sorted_a)):
            if card_order[sorted_a[i]] > card_order[sorted_b[i]]:
                return 1
            elif card_order[sorted_a[i]] < card_order[sorted_b[i]]:
                return -1

    return 0
