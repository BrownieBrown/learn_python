class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Node) -> bool:
    # dfs will return a tuple (height, is_balanced)
    def dfs(node: Node) -> (int, bool):
        # Base case: A None node has height 0 and is balanced
        if not node:
            return 0, True

        # Get depth and balanced status of left and right subtrees
        left_depth, left_balanced = dfs(node.left)
        right_depth, right_balanced = dfs(node.right)

        # Check if the current subtree is balanced
        if abs(left_depth - right_depth) > 1 or not left_balanced or not right_balanced:
            return 0, False  # Height value here doesn't matter since it's not balanced

        # Return the height of this subtree and its balanced status
        return 1 + max(left_depth, right_depth), True

    # We're interested in the balanced status of the whole tree (the second value in the tuple)
    return dfs(tree)[1]
