from collections import deque
from typing import List


# Define the Node class with properties for the node value, left, and right children
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to perform level-order traversal
def level_order_traversal(root: Node) -> List[List[int]]:
    res = []  # Initialize result list to store nodes level by level
    queue = deque([root])  # Initialize a queue and add the root node to start BFS

    while len(queue) > 0:  # Continue traversal as long as there are nodes in the queue
        n = len(queue)  # Get the number of nodes in the current level
        new_level = []  # Initialize an empty list to store the values of the nodes at the current level

        # Loop through each node in the current level
        for _ in range(n):
            node = queue.popleft()  # Remove the leftmost node from the queue
            new_level.append(node.val)  # Add the node's value to the current level list

            # Loop through the children of the node and enqueue them if they are not None
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)

        # Add the current level list to the result list
        res.append(new_level)
    return res  # Return the result list
