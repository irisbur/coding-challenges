from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_BST(root: Optional[TreeNode]) -> bool:
    vals_list = traverse_tree(root)

    for i, c in enumerate(vals_list):
        if i > 0 and c <= vals_list[i-1]:
            return False
    return True


def traverse_tree(root):
    if not root:
        return []
    if not root.right and not root.left:
        return [root.val]

    left = traverse_tree(root.left)
    right = traverse_tree(root.right)
    return left + [root.val] + right


# DFS solution
def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, l, r):
        if not node:
            return True

        if l < node.val < r:
            left = dfs(node.left, l, node.val)
            right = dfs(node.right, node.val, r)
            return left and right
        return False

    return dfs(root, -2 ** 31 - 1, 2 ** 31)