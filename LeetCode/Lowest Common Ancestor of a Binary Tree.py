class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    path_to_p = []
    path_to_q = []
    find_path_to_node(root, p, path_to_p)
    find_path_to_node(root, q, path_to_q)

    for i in range(len(path_to_p) - 1, -1, -1):
        if path_to_p[i] in path_to_q:
            return path_to_p[i]
    return root


def find_path_to_node(cur, node, path):
    if not cur:
        return False

    path.append(cur)

    if cur == node:
        return True

    if find_path_to_node(cur.left, node, path) or find_path_to_node(cur.right, node, path):
        return True

    path.pop()
    return False
