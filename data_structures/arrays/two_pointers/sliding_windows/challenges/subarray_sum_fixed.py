def subarray_sum_fixed(nums, k):
    # Initialize a variable to hold the sum of the first k elements in nums.
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]

    # Initialize a variable to hold the largest sum encountered so far,
    # which is initially set to the sum of the first k elements.
    largest = window_sum

    # Iterate through the remaining elements in nums.
    for right in range(k, len(nums)):
        # Calculate the index of the leftmost element in the current window.
        left = right - k

        # Update the sum of the window by removing the leftmost element
        # and adding the rightmost element.
        window_sum -= nums[left]
        window_sum += nums[right]

        # Update the largest sum if the current window sum is greater.
        largest = max(largest, window_sum)

    return largest


m
