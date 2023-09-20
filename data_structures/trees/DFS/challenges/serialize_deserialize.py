class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    result = []

    def dfs(node):
        # Base case: If node is None, append 'x'
        if not node:
            result.append('x')
            return

        # Append the current node's value
        result.append(str(node.val))  # Ensure that the value is converted to a string

        # Recursive calls for left and right subtrees
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return " ".join(result)


def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        # Base case: If value is 'x', return None
        if val == 'x':
            return None

        # Create a new node with the integer value
        current = Node(int(val))

        # Recursive calls to deserialize left and right subtrees
        current.left = dfs(nodes)
        current.right = dfs(nodes)

        return current

    # Create an iterator and begin the deserialization process
    return dfs(iter(s.split()))
