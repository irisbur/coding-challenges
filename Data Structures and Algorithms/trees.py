# Tree - a connected graph without cycles.
# General tree, can have maby children.

from collections import deque
class Node:
    def __init__(self, val=0, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


# Binary tree, has up to 2 children.
def invert_tree_iterative(root):
    if not root:
        return root

    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


class BinNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invert_tree_recursive(self, root):
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.invert_tree_recursive(root.left)
        self.invert_tree_recursive(root.right)
        return root


