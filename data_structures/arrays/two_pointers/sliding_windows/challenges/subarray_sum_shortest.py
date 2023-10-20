from typing import List


def subarray_sum_shortest(nums: List[int], target: int) -> int:
    # Initialize variables
    n = len(nums)
    if n == 0:
        return 0

    # window_sum keeps track of the sum within the window, length keeps track of the shortest subarray
    # length found so far, and left is the left index of the sliding window.
    window_sum, length, left = 0, len(nums), 0

    # Iterate through the list with 'right' as the current index
    for right in range(n):
        window_sum += nums[right]  # Update window_sum by adding the current element

        # Check if the sum of the current window is at least 'target'
        while window_sum >= target:
            # Update the shortest subarray length found so far
            length = min(length, right - left + 1)

            # Reduce the window size from the left
            window_sum -= nums[left]
            left += 1

    return length  # Return the shortest subarray length found
