def permutations(letters):
    def dfs(start_index, path, used, res):
        if start_index == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add a letter to permutation, mark a letter as used
            path.append(letter)
            used[i] = True
            dfs(start_index + 1, path, used, res)
            # remove a letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    ans = []
    dfs(0, [], [False] * len(letters), ans)
    return ans


"""
Solution without start_index and Set instead of List
from typing import List

def permutations(letters: str) -> List[str]:
    def dfs(path: List[str], visited: set):
        # Base case: If the current path has length equal to the original string
        if len(path) == len(letters):
            ans.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # Check if the letter at index i has been visited
            if i in visited:
                continue

            # Add the index to the visited set
            visited.add(i)

            # Append the current letter to the path and recurse
            path.append(letter)
            dfs(path, visited)
            
            # Backtrack: remove the letter from the path and mark it as not visited
            path.pop()
            visited.remove(i)

    ans = []
    dfs([], set())
    return ans

"""
