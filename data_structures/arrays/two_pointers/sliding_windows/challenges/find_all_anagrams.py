from collections import Counter
from typing import List


def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


def find_all_anagrams(original: str, check: str) -> List[int]:
    # Length of the original string
    n = len(original)

    # Length of the window, which is the same as the length of the string to check
    window_size = len(check)

    # List to hold the starting indices of anagrams of `check` in `original`
    answer = []

    # Return an empty list if the original string is too short
    if n < window_size:
        return answer

    # Iterate through `original` and slide the window to check for anagrams
    for right in range(window_size, n + 1):  # Note: Added +1 to include last window
        # Calculate the index of the leftmost element in the current window
        left = right - window_size

        # Check if the current window is an anagram of `check`
        if is_anagram(original[left:right], check):
            answer.append(left)

    return answer  # Fixed the typo here
