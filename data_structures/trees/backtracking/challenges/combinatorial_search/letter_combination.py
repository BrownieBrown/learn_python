def letter_combination(n):
    def dfs(start_index, path):
        if start_index == n:
            res.append(''.join(path))
            return
        for letter in ['a', 'b']:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res
