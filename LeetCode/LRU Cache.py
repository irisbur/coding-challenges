class CacheNode:
    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None


# The algorithm uses a doubly linked list to track the most and least used items,
# allowing constant-time access. A dictionary maps each key to its value and corresponding node.
# When accessing a value, the node is moved to the head of the list; when evicting,
# the least used item is removed from the end.
class LRUCache:
    def __init__(self, capacity: int):
        self.key_head = None
        self.key_tail = None
        self.capacity = capacity
        self.key_to_value = {}

    def get(self, key: int) -> int:
        if key in self.key_to_value:
            key_node = self.key_to_value[key][1]
            self.update_head(key_node)
            return self.key_to_value[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_value:
            self.key_to_value[key][0] = value
            self.update_head(self.key_to_value[key][1])
        else:
            if len(self.key_to_value) >= self.capacity:
                del self.key_to_value[self.key_tail.key]
                if self.key_tail.prev:
                    self.key_tail = self.key_tail.prev
                    self.key_tail.next = None
                else:
                    self.key_tail = None
                    self.key_head = None

            key_node = CacheNode(key)
            if not self.key_head:
                self.key_head = key_node
                self.key_tail = key_node
            else:
                self.update_head(key_node)
            self.key_to_value[key] = [value, key_node]

    def update_head(self, key_node):
        if key_node == self.key_head:
            return
        if key_node.prev:
            key_node.prev.next = key_node.next
        if key_node.next:
            key_node.next.prev = key_node.prev

        if key_node == self.key_tail:
            self.key_tail = self.key_tail.prev

        key_node.prev = None
        key_node.next = self.key_head
        if self.key_head:
            self.key_head.prev = key_node
        self.key_head = key_node
        if not self.key_tail:
            self.key_tail = key_node
