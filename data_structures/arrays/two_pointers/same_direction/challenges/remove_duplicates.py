from typing import List


def remove_duplicates(arr: List[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0

    slow = 0

    for fast in range(n):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1
