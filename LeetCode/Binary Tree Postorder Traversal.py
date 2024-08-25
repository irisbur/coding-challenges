from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = [root]

    while stack:
        cur = stack.pop()
        if not cur:
            break

        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

        res.append(cur.val)

    return res[::-1]

def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    left = postorder_traversal_recursive(root.left)
    right = postorder_traversal_recursive(root.right)
    return left + right + [root.val]