from collections import deque


# Question 1 - warm up
# Given and array of integers write a function that find two distint numbers that thiers sum is zero
# and return their indices, if there are a few options you can return one.
# if there's no such pair, return null.
# Write an algorithm that runs in O(n) time complexity
def two_sum(nums):
    int_to_dict = {}
    for n in nums:
        int_to_dict[n] = int_to_dict.get(n, 0) + 1

    for i in nums:
        neg = -1 * nums[i]
        if neg != 0 and neg in nums:
            return [i, int_to_dict[neg]]

    return None


# Question 2 - Look and Say
# number, n
# 2, 3 : 3112
# 211, 1 -> 1221
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


# Island map - count steps from S to D on a n*m grid, if you cant reach the grid return -1.
# at each step you can move up, down, keft or right only on empty cells.
# '.' - empty cell
# '*' - flooded cell
# 'X' - rock
# at every move the flooded cell flood all their empty neighbors.
def count_steps(island_map):
    n, m = len(island_map), len(island_map[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    si, sj = find_initial_position(island_map)
    qe = deque([(si, sj, 0)])
    visited = {(si, sj)}
    flooded = find_initial_flood(island_map)
    while qe:
        ci, cj, step = qe.popleft()
        flooded = flood(island_map, flooded)
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if is_position_valid(ni, nj, n, m) and island_map[ni][nj] == "D":
                return step + 1
            elif is_position_valid(ni, nj, n, m) and island_map[ni][nj] == ".":
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
# write a function that recives a hand and returns the type of the hand,
# the function recives string with len 5 representing 5 cards from 2-9, J, Q, K
# ignore 10 and assume all input is valid.
# the types are: "Four of a Kind", "Full House", "Three of a kind", "Two Pair", "Pair"
# and if you don't match any of these return "High Card".
def get_hand_type(hand):
    cntr = {}
    for c in hand:
        cntr[c] = cntr.get(c, 0) + 1

    counts = [v for k, v in cntr.items()]
    counts.sort()

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
# write a function that recives handA and handB and returns 1 if handA is stronger, -1 if B is stronger
# 0 if there's a tie.
# base the srtengths accoding to the card type, if they're the same type compare them alphabetically in dsc order.
def stronger_card(handA, handB):
    type_to_strength = {"Four of a Kind": 5, "Full House": 4,
                        "Three of a Kind": 3, "Two Pair": 2, "Pair": 1, "High Card": 0}
    type_a = get_hand_type(handA)
    type_b = get_hand_type(handB)

    if type_to_strength[type_a] > type_to_strength[type_b]:
        return 1
    elif type_to_strength[type_a] < type_to_strength[type_b]:
        return -1
    else:
        handA.sort(reverse=True)
        handB.sort(reverse=True)
        for i in range(len(handA)):
            if handA[i] > handB[i]:
                return 1
            elif handA[i] < handB[i]:
                return -1
    return 0
