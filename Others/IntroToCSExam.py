def q3():
    concat_strings = lambda a: ''.join(a)

    assert concat_strings(['hello', ' ', 'world']) == 'hello world'
    assert concat_strings(['h', 'e', 'l', 'l', 'o']) == 'hello'
    assert concat_strings([]) == ''


def alternate_helper(n, increasing):
    if n < 10:
        return True

    last_digit = n % 10
    next_to_last_digit = (n % 100) // 10

    if ((increasing and next_to_last_digit < last_digit) or
            (not increasing and next_to_last_digit > last_digit)):
        return alternate_helper(n // 10, not increasing)
    return False


def alternate(n):
    last_digit = n % 10
    next_to_last_digit = (n % 100) // 10
    return alternate_helper(n, next_to_last_digit < last_digit)


def check_q4():
    assert alternate(1324) is True  # (1 < 3 > 2 < 4)
    assert alternate(1234) is False  # (1 < 2 < 3 < 4)
    assert alternate(2143) is True  # (2 > 1 < 4 > 3)
    assert alternate(5432) is False  # (5 > 4 > 3 > 2)
    assert alternate(4233) is False  # (4 > 2 < 3 = 3)


def q5():
    a = [[i] * i for i in range(2)]
    b = a
    c = b
    d = c
    e = [a, b, c]
    f = e[:]
    print(f)
    a[0] = [2, 2]
    print(e)
    print(f)


def process_data(data):
    result = []
    for i, item in enumerate(data):
        if i % 2:
            try:
                result.append(100 / (item - 1))
            except ZeroDivisionError:
                print("a")
            except Exception:
                print("b")
            except TypeError:
                print("c")
        else:
            try:
                result.append(item + "appended")
            except TypeError:
                print("d")
            finally:
                print("e")


def check_q6():
    process_data(["a", 1, "a", 2, 'a'])  # "eaee"
    process_data(['a', 2, 2, 1, 1])  # "edeade
    process_data(['a', 2, 2, "2", '2'])  # "edebde


def q7_infinite_cycle(lst):
    while True:
        for x in lst:
            yield x


# Q8
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sorted_array_to_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    return Tree(arr[mid],
                sorted_array_to_bst(arr[:mid]),
                sorted_array_to_bst(arr[mid + 1:]))


# Q9
def find_target_indexes(vals):
    index_map = {}
    for i, num in enumerate(vals):
        if num in index_map and i == index_map[num]:
            return True
        index_map[num] = i * num
    return False


# vals = [0 ,2, 2] - > True

# Q10
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_duplicates(head):
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next  # DO NOT FORGET TO MOVE TO NEXT NODE!!


# convert python list to linked list
def list2linkedlist(lst):
    if not lst:
        return None

    head = Node(lst[0])
    prev = head
    for val in lst[1:]:
        new_node = Node(val)
        prev.next = new_node
        prev = new_node
    return head


# convert linked list to python list
def linkedlist2list(ll):
    lst = []
    cur = ll
    while cur:
        lst.append(cur.data)
        cur = cur.next
    return lst


head = list2linkedlist([1, 1, 1, 2, 3, 3, 1])
remove_duplicates(head)
assert linkedlist2list(head) == [1, 2, 3, 1]


# Q11
# Write a function that returns the diameter of a binary tree given the root.
def diameter_of_binary_tree(root):
    return helper(root)[0]


def helper(root):
    if not root:
        return 0, -1

    dl, ll = helper(root.left)
    dr, lr = helper(root.right)
    return max(dl, max(dr, 2 + ll + lr)), max(ll, lr) + 1


# Q12
def find_palindromes(string, k):
    if k > len(string):
        return []

    pass


# Q13
class Plane:
    def __init__(self, rows, cols, baggage_allowance):
        self.rows = rows
        self.cols = cols
        self.baggage_allowance = baggage_allowance
        self.passengers_map = {}  # passenger to [seat, [suitcases id]]
        self.seats_map = {}  # seat to passenger
        self.bags_map = {}  # bag_id -> [weight, passenger_id]

    def register(self, passenger_id, seat) -> bool:
        if self.is_seat_valid(seat) and seat not in self.seats_map:
            self.seats_map[seat] = passenger_id
            if passenger_id not in self.passengers_map:
                self.passengers_map[passenger_id] = [seat, []]
            else:
                old_seat, bags = self.passengers_map[passenger_id]
                del self.seats_map[old_seat]
                self.passengers_map[passenger_id] = [seat, bags]
            return True
        return False

    def deregister(self, passenger_id) -> bool:
        if passenger_id in self.passengers_map:
            seat, bags = self.passengers_map[passenger_id]
            del self.passengers_map[passenger_id]
            del self.seats_map[seat]
            for bag in bags:
                del self.bags_map[bag]
            return True
        return False

    def add_suitcase(self, suitcase_id, weight, passenger_id) -> bool:
        if ((suitcase_id not in self.bags_map) and (passenger_id in self.passengers_map)
                and (self.get_passenger_weight(passenger_id) + weight) < self.baggage_allowance):
            self.passengers_map[passenger_id][1].append(suitcase_id)
            self.bags_map[suitcase_id] = [weight, passenger_id]
            return True
        return False

    def remove_suitcase(self, suitcase_id) -> bool:
        if suitcase_id in self.bags_map:
            passenger = self.bags_map[suitcase_id][1]
            del self.bags_map[suitcase_id]
            self.passengers_map[passenger][1].remove(suitcase_id)
            return True
        return False

    def get_passenger_weight(self, passenger_id):
        bags = self.passengers_map[passenger_id][1]
        weight = 0
        for bag in bags:
            weight += self.bags_map[bag][0]
        return weight

    def is_seat_valid(self, seat):
        i, j = seat
        return 0 <= i < self.rows and 0 <= j <= self.cols


def check_q13():
    plane = Plane(10, 4, 25)
    # Register the passenger "1" to locations (2, 2) and (2, 3)
    assert plane.register(1, (2, 3)) == True
    # Passenger "1" registered seat (2,3)
    assert plane.register(1, (2, 2)) == True
    # Passenger "1" moved to seat (2,2)
    assert plane.register(2, (2, 2)) == False
    # Seat not empty
    assert plane.register(1, (2, 2)) == False
    # Passenger "1" is already sitting there
    assert plane.deregister(1) == True
    assert plane.register(2, (2, 2)) == True
    # Passenger "1" is not registered
    assert plane.add_suitcase(100, 20, 1) == False
    assert plane.add_suitcase(100, 20, 2) == True
    # Total weight for passenger "2" would be too big.
    assert plane.add_suitcase(200, 10, 2) == False
    assert plane.remove_suitcase(100) == True
    assert plane.remove_suitcase(200) == False
    # Suitcase is not loaded
    assert plane.add_suitcase(200, 10, 2) == True
    assert plane.add_suitcase(200, 20, 2) == False  # Suitcase already loaded (weight is not changed)
    assert plane.register(1, (2, 3)) == True
    assert plane.deregister(2) == True
    assert plane.add_suitcase(200, 10, 1) == True
    # Suitcase was removed when "2" deregistered

# Q14
# Q15
# Q16
