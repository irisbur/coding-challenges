# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# There are several variant of this question, this one is problem 21 in LeetCode.
def merge_two_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    c1, c2 = list1, list2
    if c2.val < c1.val:
        c2_next = c2.next
        c2.next = list1
        list1, c1 = c2, c2
        c2 = c2_next

    while c2 and c1.next:
        if c1.val <= c2.val < c1.next.val and c1.next:
            c2_next = c2.next
            c2.next = c1.next
            c1.next = c2
            c2 = c2_next
            c1 = c1.next
        else:
            c1 = c1.next

    if c2:
        c1.next = c2

    return list1
