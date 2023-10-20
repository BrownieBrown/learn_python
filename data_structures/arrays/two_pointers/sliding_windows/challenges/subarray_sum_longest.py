from typing import List


def subarray_sum_longest(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return 0

    window_sum, length = 0, 0
    left = 0

    for right in range(n):
        window_sum += nums[right]
        while window_sum > target:
            window_sum -= nums[left]
            left += 1

        length = max(length, right - left + 1)

    return length
