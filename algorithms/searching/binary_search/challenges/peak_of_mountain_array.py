from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            # If the mid-element is less than its next element,
            # then the peak lies in the right half of the array.
            left = mid + 1
        else:
            # Otherwise, the peak is in the left half.
            right = mid

    # When the loop breaks, left will be at the peak of the mountain.
    return left
