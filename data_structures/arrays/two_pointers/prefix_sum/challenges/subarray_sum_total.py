from collections import Counter  # Importing Counter from collections module
from typing import List  # Importing List for type hinting


def subarray_sum_total(arr: List[int], target: int) -> int:
    n = len(arr)  # Get the length of the array
    if n == 0:  # If the array is empty, return 0
        return 0

    # Initialize Counter object to keep track of prefix sums
    prefix_sums = Counter()

    # Start with the sum of an empty subarray, which is 0
    # There is one such sum, hence, prefix_sums[0] = 1
    prefix_sums[0] = 1

    curr_sums = 0  # Initialize variable to hold the running sum
    count = 0  # Initialize counter for subarrays summing to target

    for index in range(n):  # Loop through the array
        curr_sums += arr[index]  # Update the running sum
        compliment = curr_sums - target  # Calculate the complement

        # If the complement is present in the Counter, add its count to 'count'
        if compliment in prefix_sums:
            count += prefix_sums[compliment]

        # Update prefix_sums Counter; if curr_sums is already there, increment its value by 1
        # If not, it will be added with a value of 1
        prefix_sums[curr_sums] += 1

    return count  # Return the final count
