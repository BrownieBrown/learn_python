class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
    if root is None:
        return 0

    left_depth = tree_max_depth_counting_edges(root.left)
    right_depth = tree_max_depth_counting_edges(root.right)

    return 1 + max(left_depth, right_depth)


def tree_max_depth_counting_edges(root: Node) -> int:
    def dfs(node):
        # null node adds no depth
        if not node:
            return 0
        # num nodes in the longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(node.left), dfs(node.right)) + 1

    return dfs(root) - 1 if root else 0
