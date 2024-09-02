from collections import deque
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None

    qe = deque([node])
    node_copy = Node(node.val)
    visited = {node.val: node_copy}

    while qe:
        cur = qe.popleft()
        cur_copy = visited[cur.val]

        for neighbor in cur.neighbors:
            if neighbor.val not in visited:
                neighbor_copy = Node(neighbor.val)
                visited[neighbor.val] = neighbor_copy
                qe.append(neighbor)

            cur_copy.neighbors.append(visited[neighbor.val])

    return node_copy
