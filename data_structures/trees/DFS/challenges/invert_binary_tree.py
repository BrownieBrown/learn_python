class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(tree: Node) -> Node:
    def dfs(node):
        if not node:
            return None

        node.left, node.right = node.right, node.left
        dfs(node.left)
        dfs(node.right)

        return node

    return dfs(tree)


"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    if tree is None:
        return None
    return Node(tree.val, invert_binary_tree(tree.right), invert_binary_tree(tree.left))
"""
