class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_bst(bst: Node, val: int) -> Node:
    if not bst:
        return Node(val)
    if bst.val < val:
        bst.right = insert_bst(bst.right, val)
    elif bst.val > val:
        bst.left = insert_bst(bst.left, val)

    return bst
