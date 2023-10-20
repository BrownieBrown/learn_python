from typing import List


def subarray_sum(arr: List[int], target: int) -> List[int]:
    n = len(arr)  # Get the length of the input array
    if n == 0:  # Check for an empty array and return an empty list
        return []

    # Initialize prefix_sums dictionary with the first key-value pair (0: 0)
    prefix_sums = {0: 0}
    cur_sum = 0  # Initialize running sum variable

    for index in range(n):  # Iterate through the input array
        cur_sum += arr[index]  # Add each element to the running sum
        complement = cur_sum - target  # Calculate the complement needed to form a subarray summing to 'target'

        # Check if the complement exists in the prefix_sums dictionary
        if complement in prefix_sums:
            # If it does, return the start and end indices of the subarray
            return [prefix_sums[complement],
                    # Index + 1 because prefix_sums stores the index one position ahead of the actual subarray
                    index + 1]

        # Update the prefix_sums dictionary with the running sum
        prefix_sums[cur_sum] = index + 1  # Again, index + 1 because we are looking at sums up to the next index
