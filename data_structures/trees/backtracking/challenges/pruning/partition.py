from typing import List


def partition(s: str) -> List[List[str]]:
    # Initialize an empty list to store the final list of palindrome partitions
    ans = []

    # Get the length of the input string
    n = len(s)

    # Helper function to check if a word is a palindrome
    def is_palindrome(word) -> bool:
        # Returns True if word is equal to its reverse, else False
        return word == word[::-1]

    # Core backtracking function to find palindrome partitions
    def dfs(start: int, cur_path: List[str]):
        # Base condition: if the current start index has reached the end of the string,
        # it means the current path (cur_path) is a valid partition, so add it to the result
        if start == n:
            ans.append(cur_path[:])
            return

        # Loop from the current start index to the end of the string
        for end in range(start + 1, n + 1):
            # Extract the current prefix substring
            prefix = s[start: end]
            # If the prefix is a palindrome, continue with the backtracking by moving the start index to end
            if is_palindrome(prefix):
                dfs(end, cur_path + [prefix])

    # Start the backtracking process from the first character of the string
    dfs(0, [])

    # Return the final result
    return ans
