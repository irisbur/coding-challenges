from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    if not root.left and not root.right:
        return [[root.val]]

    result = []
    de = deque([root])
    levels = {root: 0}

    while de:
        cur = de.popleft()
        level = levels[cur]

        if len(result) < (level + 1):
            result.append([cur.val])
        else:
            result[level].append(cur.val)

        if cur.left:
            de.append(cur.left)
            levels[cur.left] = level + 1
        if cur.right:
            de.append(cur.right)
            levels[cur.right] = level + 1

    return result
