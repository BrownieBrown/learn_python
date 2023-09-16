class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_tree_node(root: Node) -> int:
    # Inner recursive function to traverse the tree
    def dfs(node, max_sofar):
        # Base case: if the node is None (or not present), we return 0
        if not node:
            return 0

        total = 0  # Initialize a counter to keep track of visible nodes

        # If the current node's value is greater than or equal to the maximum value
        # encountered so far in the path, then it's visible.
        # We increment our counter.
        if node.val >= max_sofar:
            total += 1

        # Recursive call for the left child:
        # We pass the current node's left child and the maximum of
        # the current maximum value and the node's value to the recursive call.
        # This ensures that for each path, we're always tracking the highest value encountered.
        total += dfs(node.left, max(max_sofar, node.val))

        # Similarly, recursive call for the right child:
        total += dfs(node.right, max(max_sofar, node.val))

        # Return the total visible nodes for the current subtree rooted at 'node'
        return total

    # The outer function begins here.
    # We initiate the traversal starting from the root with
    # the smallest possible value as the initial maximum (-infinity).
    # This ensures the root node is always considered visible.
    return dfs(root, -float('inf'))
