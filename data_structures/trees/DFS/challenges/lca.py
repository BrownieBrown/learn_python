class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
cases: 
1. The node-x is null
2. The node-x is either node1 or node2
3. The node-x is neither node1 nor node2
    a. If both subtrees return non-null nodes: return the current node itself
    b. If both subtrees return null nodes: return null
    c. If exactly one of the subtrees returns a non-null node and the other returns a null node: return the non-null node
"""


def lca(root, node1, node2):
    if not root:
        return

    # case 2
    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # case 1
    if left and right:
        return root

    # at this point, left and right can't be both non-null since we checked above
    # case 3a and 3b, report target node or LCA back to parent
    if left:
        return left
    if right:
        return right

    # case 3, not found return null
    return None
