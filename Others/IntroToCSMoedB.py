'''
Q1:
(1) not old_head or not old_head.next
(2) cur.next and cur.next.next
(3) cur.next
(4) None
(5) old_head
'''


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):  # iterates over values
        # omitted (only used for examples)
        current = self.head
        while current:
            yield current.data
            current = current.next


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def build_ll(lst):  # convert python list to linked list
    if not lst:
        return LinkedList()

    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next

    return LinkedList(head)


def rotate_right(lnklst):
    old_head = lnklst.head
    if not old_head or not old_head.next:
        return lnklst

    cur = old_head
    while cur.next and cur.next.next:
        cur = cur.next

    new_head = cur.next
    cur.next = None
    new_head.next = old_head

    lnklst.head = new_head
    return lnklst


def check_q1():
    # Test cases:
    assert list(rotate_right(build_ll([]))) == []
    assert list(rotate_right(build_ll([1]))) == [1]
    assert list(rotate_right(build_ll([1, 2]))) == [2, 1]
    assert list(rotate_right(build_ll([1, 2, 3, 4]))) == [4, 1, 2, 3]
    assert list(rotate_right(rotate_right(build_ll([1, 2, 3, 4])))) == [3, 4, 1, 2]
    assert list(rotate_right(rotate_right(rotate_right(build_ll([1, 2, 3, 4]))))) == [2, 3, 4, 1]


'''
Q2:
when k is a constant. 
x = int(sqrt(n)) O(1)
while x >= 0 will run O(sqrt(n)) times
since k is constant he inner loop will take O(1) steps, so the total runtime is O(1)

if n is constant, the inner and outer loop will take cosnt time, all rest of ops are const time 
so we get cosnt runtime complexity
'''

'''
Q3:

'''


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_to_list(tree):
    if not tree:
        return None
    return [tree.data] + [tree_to_list(tree.left)] + [tree_to_list(tree.right)]


def check_q3():
    assert tree_to_list(None) is None

    t = Tree(3, Tree(1), Tree(4, None, Tree(2)))
    print(tree_to_list(t))
    assert tree_to_list(t) == [3,
                               [1, None, None],
                               [4, None, [2, None, None]]]

    t = Tree(1)
    assert tree_to_list(t) == [1, None, None]


'''
Q4:
2 lists with len(n/2): O(n^2)
n/2 lists with len(2): O(n)
sqrt(n) lists with len(sqrt(n)): O(n^(3/2))
'''

'''
Q5:
O(n log n) - since we do op in len(n) in every call and we will do 
log n recursive calls. 
'''

'''
Q6:
(1) factors not in sublists 
(2) sublists[factors]
(3) sublists[factors]
(4) [(key, value) for sublists.items()] or just sublists.items() 
'''


def check_q6():
    def factor_count(n):
        return sum((i != n // i) + 1
                   for i in range(1, int(n ** 0.5) + 1)
                   if n % i == 0)

    def groupby_factor_count(lst):
        sublists = {}
        for k in lst:
            factors = factor_count(k)
            if factors not in sublists:
                sublists[factors] = []
            sublists[factors].append(k)
        yield from [(key, value) for key, value in sublists.items()]

    lst = [12, 18, 20, 28, 30, 36, 40, 45, 50, 60, 72, 80]
    assert list(groupby_factor_count(lst)) == [
        (6, [12, 18, 20, 28, 45, 50]),
        (8, [30, 40]),
        (9, [36]),
        (12, [60, 72]),
        (10, [80]),
    ]

    lst = [15, 60, 134, 67]
    assert list(groupby_factor_count(lst)) == [
        (4, [15, 134]),
        (12, [60]),
        (2, [67]),
    ]


'''
Q7
'''
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        # Check if 'other' is an instance of Tree
        if not isinstance(other, Tree):
            return False
        # Check if data, left, and right children are equal
        return (self.data == other.data and
                self.left == other.left and
                self.right == other.right)


def robbing_nodes(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1

    t1.left = robbing_nodes(t1.left, t2.left)
    t1.right = robbing_nodes(t1.right, t2.right)

    return t1

def check_q7():
    t1 = Tree(1, Tree(2, None, Tree(5)), None)
    t2 = Tree(10,
              Tree(20, Tree(40), None),
              Tree(30, None, Tree(50)))
    t3 = Tree(1,
              Tree(2, Tree(40), Tree(5)),
              Tree(30, None, Tree(50)))
    assert robbing_nodes(t1, t2) == t3

    t1 = Tree(4, None, Tree(6, Tree(7), None))
    t2 = Tree(8,
              Tree(3),
              Tree(9, None, Tree(5)))
    t3 = Tree(4,
              Tree(3),
              Tree(6, Tree(7), Tree(5)))
    assert robbing_nodes(t1, t2) == t3

    t1 = Tree(5, Tree(3, None, Tree(4)), None)
    t2 = Tree(1, Tree(2, Tree(6), Tree(7)), None)
    t3 = Tree(5,
              Tree(3, Tree(6), Tree(4)),
              None)
    assert robbing_nodes(t1, t2) == t3

# 12645432
# 01234567
# nd = 8,
# 3, 5   2 6   1 7   0 8



'''
Q8:
(1) num_digits // 2 - 1
(2) num_digits - 1 - i
(3) str(n)[left_index]
(4) str(n)[right_index]
'''

'''
Q9:
'''


def similar_topo(m, n):
    m_count = count_topo(m)
    n_count = count_topo(n)
    return m_count == n_count


def count_topo(v):
    p_v_track = []
    for i, c in enumerate(v):
        if 0 < i < (len(v) - 1):
            if c > v[i-1] and c > v[i+1]:
                p_v_track.append("p")
            elif c < v[i-1] and c < v[i+1]:
                p_v_track.append("v")
    return p_v_track


def check_q9():
    assert similar_topo("132","1346753") == True
    assert similar_topo("3214","54323678") == True
    assert similar_topo("1","1221") == True
    assert similar_topo("13232","132232") == False
    assert similar_topo("1436","6341") == False



'''
Q10:
'''
def close_pairs(numbers):
    num_map = {}
    for i, n in enumerate(numbers):
        if n not in num_map:
            num_map[n] = [i]
        else:
            num_map[n].append(i)

    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            for l, c in enumerate(numbers):
                if i != j and j != l and l != i:
                    d = (a+b) - c

                    if d in numbers:
                        k = [k for k in num_map[d] if k not in [i, j, l]]
                        if k:
                            return (a, b), (c, d)
                    elif d + 1 in numbers:
                        k = [k for k in num_map[d+1] if k not in [i, j, l]]
                        if k:
                            return (a, b), (c, d + 1)
                    elif d - 1 in numbers:
                        k = [k for k in num_map[d-1] if k not in [i, j, l]]
                        if k:
                            return (a, b), (c, d - 1)

def check_q10():
    # print(close_pairs([10, 15, 3, 7, 8, 5, 12])) # ((10, 5), (7, 8))
    numbers = [1, 2, 4, 9, 19, 29]
    print(close_pairs(numbers))
    print(close_pairs([10, 15, 3, 7, 5])) # ((10, 3), (7, 5))
    print(close_pairs([1, 2, 2, 3])) # ((3, 5), (3, 5))
    print(close_pairs([1, 2, -2, -3])) # ((1, -2), (-3, 2))



"""
Change Machine
"""
class ChangeMachine:
    def __init__(self, coin_vals):
        self.coins = {val:0 for val in coin_vals} # inventory dictionary.

    def modify_money(self, coin_val, count):
        if coin_val not in self.coins:
            return False

        if self.coins[coin_val] + count >= 0:
            self.coins[coin_val] += count
            return True
        return False

    def check_low_inventory(self, threshold):
        low_inv_map = {}
        for coin in self.coins:
            if self.coins[coin] < threshold:
                low_inv_map[coin] = self.coins[coin]
        return low_inv_map

    def get_change(self, amount, strategy="min"):
        if strategy == "min":
            return self.get_change_min(amount)
        else:
            return self.get_change_max(amount)

    def get_change_min(self, amount):
        if amount == 0:
            return {}

        dp = [{} for _ in range(amount + 1)]
        sorted_coin_vals = sorted(self.coins.keys())

        for val in range(1, amount + 1):
            for coin in sorted_coin_vals:
                if coin > val:
                    break

                if val - coin == 0 or dp[val - coin] != {}:
                    previous_combo = dp[val - coin].copy()
                    if previous_combo.get(coin, 0) < self.coins[coin]:
                        new_combo = previous_combo.copy()
                        new_combo[coin] = new_combo.get(coin, 0) + 1

                        if dp[val] == {} or sum(new_combo.values()) < sum(dp[val].values()):
                            dp[val] = new_combo

        if dp[amount] != {}:
            for c in dp[amount]:
                self.coins[c] -= dp[amount][c]
            return dp[amount]
        return None

    def get_change_max(self, amount):
        dp = [{} for _ in range(amount + 1)]
        sorted_coin_vals = sorted(self.coins.keys(), reverse=True)

        for val in range(1, amount + 1):
            for coin in sorted_coin_vals:
                if coin > val:
                    continue

                if val - coin == 0 or dp[val - coin] != {}:
                    previous_combo = dp[val - coin].copy()
                    if previous_combo.get(coin, 0) < self.coins[coin]:
                        new_combo = previous_combo.copy()
                        new_combo[coin] = new_combo.get(coin, 0) + 1

                        if dp[val] == {} or sum(new_combo.values()) > sum(dp[val].values()):
                            dp[val] = new_combo

        if dp[amount] != {}:
            for c in dp[amount]:
                self.coins[c] -= dp[amount][c]
            return dp[amount]
        return None

def check_coin_machine():
    coin_vals = [2, 10, 1000, 100]
    machine = ChangeMachine(coin_vals)
    assert machine.modify_money(2, 300) == True
    assert machine.modify_money(10, 300) == True
    assert machine.modify_money(100, 300) == True
    assert machine.modify_money(100, -100) == True
    assert machine.modify_money(100, -300) == False # Not enough
    assert machine.modify_money(1000, 3) == True
    assert machine.modify_money(3, 10) == False # Bad coin value
    assert machine.modify_money(2, 0) == True # Valid, but doesn't change anything
    assert machine.modify_money(3, 0) == False # Bad coin value
    assert machine.check_low_inventory(3) == {}
    assert machine.check_low_inventory(4) == {1000:3}
    assert machine.check_low_inventory(4) == {1000:3}
    assert machine.get_change(1000) == {1000:1} # or with "min"
    assert machine.get_change(3) == None # 3%2 != 0
    assert machine.get_change(3000000) == None # Not enough
    assert machine.get_change(1000, "max") == {2:300,10:40}
    assert machine.get_change(36) == None # No 2 valued coins left
    assert machine.check_low_inventory(4) == {1000:2,2:0} # coins were removed
    assert machine.get_change(0) == {}
