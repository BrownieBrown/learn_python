from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: Node) -> List[int]:
    result = []
    queue = deque([root])

    while queue:
        new_level = []
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)

            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

        result.append(new_level[-1])

    return result
