from collections import defaultdict


def longest_substring_without_repeating_characters(s: str) -> int:
    longest = 0
    left = 0
    counter = defaultdict(int)
    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest
