from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(start_index: int, path: List[int]):
        res.append(path[:])

        for i in range(start_index, len(nums)):
            num = nums[i]
            path.append(num)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res
