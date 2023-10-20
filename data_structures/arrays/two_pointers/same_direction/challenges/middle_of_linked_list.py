class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def middle_of_linked_list(head: Node) -> int:
    if not head:
        raise ValueError("The linked list is empty. Cannot find the middle element.")

    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.val
