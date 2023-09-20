from typing import List

PHONE = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(start_index, path):
        if start_index == len(digits):
            res.append(''.join(path))
            return

        for letter in PHONE[digits[start_index]]:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res
