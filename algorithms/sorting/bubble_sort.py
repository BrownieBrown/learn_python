from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Iterate through all list elements in reversed order
    for i in reversed(range(n)):

        # Track whether a swap occurred in this pass
        swapped = False
        for j in range(i):

            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # If no two elements were swapped, the list is sorted
        if not swapped:
            return unsorted_list

    return unsorted_list
