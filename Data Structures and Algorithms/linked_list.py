
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    size = 0
    head = None

    def get_size(self):
        return self.size

    def find(self, data):
        curr = self.head
        while curr:
            if curr.val == data:
                return curr
            curr = curr.next
        return None

    def add(self, data):
        node = ListNode(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def add_to_tail(self, data):
        node = ListNode(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    def remove(self, data):
        curr = self.head
        if self.head.val == data:
            self.head = self.head.next
            self.size -= 1
            return True

        while curr.next:
            if curr.next.val == data:
                curr.next = curr.next.next
                self.size -= 1
                return True

            curr = curr.next
        return False


def iterative_reverse(head):
    prev, curr = None, head

    while curr:
        new_curr = curr.next
        curr.next = prev
        prev = curr
        curr = new_curr
    return prev


def recursive_reverse(head):
    if not head or not head.next:
        return head

    new_head = recursive_reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

