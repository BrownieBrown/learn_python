from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        # gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            # swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1

    return unsorted_list
