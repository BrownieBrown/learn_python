def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    # Using 'or' for short-circuiting: If the left call finds the node, it will return it.
    # If not, it will proceed to call the right DFS.
    return dfs(root.left, target) or dfs(root.right, target)
