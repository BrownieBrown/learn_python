from typing import List


def move_zeros(nums: List[int]) -> None:
    n = len(nums)
    slow = 0

    for fast in range(n):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
