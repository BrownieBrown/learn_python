from typing import List


def generate_parentheses(n: int) -> List[str]:
    # The dfs (depth-first search) function is the core of our backtracking algorithm.
    # We'll use it to explore different combinations of parentheses.
    def dfs(start_index: int, path: List[str], open_count: int, close_count: int, res: List[str]):
        # If we've reached two * n characters in our current path (which means n open and n close parentheses),
        # we append the current path to our result list and return.
        if start_index == 2 * n:
            res.append(''.join(path))
            return

        # If we haven't used up all the open parentheses (open_count < n),
        # we add an open parenthesis to our current path and recurse further.
        if open_count < n:
            path.append('(')
            dfs(start_index + 1, path, open_count + 1, close_count, res)
            path.pop()  # backtrack: remove the last added '('

        # If the number of close parentheses used so far is less than the number of open parentheses used,
        # we can add a close parenthesis to our current path and recurse further.
        if close_count < open_count:
            path.append(')')
            dfs(start_index + 1, path, open_count, close_count + 1, res)
            path.pop()  # backtrack: remove the last added ')'

    # This is our result list, where we'll store all valid combinations of parentheses.
    ans = []

    # Start the dfs function from index 0, with no parentheses added so far, and with both open_count and close_count
    # set to 0.
    dfs(0, [], 0, 0, ans)

    return ans
