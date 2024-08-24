from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
