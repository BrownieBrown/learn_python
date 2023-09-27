from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_min_depth(root: Node) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0

    while queue:
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()

            if node.left is None and node.right is None:
                return depth

            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

        depth += 1

    return depth
