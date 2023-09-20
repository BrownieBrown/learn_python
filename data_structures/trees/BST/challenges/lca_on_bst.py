class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_on_bst(bst: Node, p: int, q: int) -> int:
    if p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p, q)
    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
    else:
        return bst.val
