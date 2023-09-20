from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    result = []

    def dfs(node: Node, path: str):
        if not node:
            return

        # Add the current node's value to the path
        current_path = path + str(node.val)

        # Check if it's a leaf node (no children)
        if not node.children:
            result.append(current_path)
            return

        # Recurse for each child
        for child in node.children:
            dfs(child, current_path + "->")  # The "->" can be any delimiter you want

    dfs(root, "")
    return result
