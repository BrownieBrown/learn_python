class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: Node) -> bool:
    def dfs(node, min_val, max_val):
        # empty nodes are always valid
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        # see notes below
        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, '-inf', 'inf')  # root is always valid
