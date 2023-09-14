from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    left, right, result = 0, len(arr) - 1, -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result
