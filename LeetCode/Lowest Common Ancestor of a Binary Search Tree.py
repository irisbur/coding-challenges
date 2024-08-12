# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor_recursive(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None

    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor_recursive(root.left, p, q)

    if root.val < p.val and root.val < q.val:
        return lowest_common_ancestor_recursive(root.right, p, q)

    return root

def lowest_common_ancestor_iterative(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None

    curr = root
    while curr.val and ((curr.val > p.val and curr.val > q.val) or (curr.val < p.val and curr.val < q.val)):
        if curr.val > p.val and curr.val > q.val:
            curr = curr.left
        else:
            curr = curr.right

    return curr


