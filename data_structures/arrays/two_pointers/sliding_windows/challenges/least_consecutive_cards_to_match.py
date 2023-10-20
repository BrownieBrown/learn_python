from collections import defaultdict
from typing import List


def least_consecutive_cards_to_match(cards: List[int]) -> int:
    n = len(cards)
    if n == 0:
        return -1

    left, length = 0, n
    cards_seen = defaultdict(int)  # Initialize dictionary with default integer value 0
    found = False  # Flag to indicate if we found a pair of consecutive cards

    for right in range(n):
        right_number = cards[right]
        left_number = cards[left]

        cards_seen[right_number] += 1  # Increment card count

        while cards_seen[right_number] > 1:  # Check for duplicates
            found = True  # Set the flag to True
            length = min(length, right - left + 1)  # Update the minimum length
            cards_seen[left_number] -= 1  # Remove card count from the left
            if cards_seen[left_number] == 0:  # Optionally remove the key if count is zero
                del cards_seen[left_number]
            left += 1  # Move the window

    return length if found else -1  # Return -1 if no pair of consecutive cards were found


# Example usage
print(least_consecutive_cards_to_match([1, 2, 3, 4, 4, 5]))
print(least_consecutive_cards_to_match([1, 2, 3]))
