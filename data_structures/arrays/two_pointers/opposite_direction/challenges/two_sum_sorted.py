from typing import List


def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    n = len(arr)
    if n == 0:
        return []

    left = 0
    right = n - 1

    while left != right:
        left_numb, right_number = arr[left], arr[right]
        current_sum = left_numb + right_number  # Calculating the sum once to avoid repetitive calculations

        if current_sum == target:
            return [left, right]  # Return immediately once the target sum is found

        if current_sum > target:
            right -= 1

        if current_sum < target:
            left += 1

    return []
