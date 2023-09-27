from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root: Node) -> List[List[int]]:
    res = []
    queue = deque([root])
    depth = 0  # To keep track of the level we are at

    while queue:  # As long as there are nodes in the queue
        new_level = []
        n = len(queue)

        # Process all nodes at the current level
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)

            # Enqueue the children for the next level
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

        # If we're at an odd level, reverse the order of the nodes
        if depth % 2 != 0:
            new_level.reverse()

        res.append(new_level)
        depth += 1  # Move on to the next level

    return res
