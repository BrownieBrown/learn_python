class Node:
    def __init__(self, val, next=None):  # Node class definition with value and next pointer
        self.val = val
        self.next = next


def has_cycle(nodes: Node) -> bool:
    if not nodes:  # If the list is empty, return False
        return False

    # Initialize slow and fast pointers to the head of the list
    slow_pointer, fast_pointer = nodes, nodes

    # Run until the fast pointer reaches the end of the list
    while fast_pointer.next and fast_pointer.next.next:
        # Move the fast pointer two steps ahead
        fast_pointer = fast_pointer.next.next
        # Move the slow pointer one step ahead
        slow_pointer = slow_pointer.next

        # If they meet at some point, then a cycle exists
        if slow_pointer == fast_pointer:
            return True

    return False  # Return False if loop exits, meaning no cycle exists
