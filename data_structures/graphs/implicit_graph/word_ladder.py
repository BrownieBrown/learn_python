from collections import deque
from string import ascii_letters
from typing import List


def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    # Quick-edge case checks
    if begin == end:
        return 0
    if end not in word_list:
        return -1  # or some indicator that it's not possible

    unvisited_words = set(word_list)

    def get_neighbors(word: str) -> List[str]:
        """Generate all unvisited neighbors of a given word."""
        unvisited_neighbors = []
        for i in range(len(word)):
            for c in ascii_letters:
                next_word = word[:i] + c + word[i + 1:]
                if next_word in unvisited_words:
                    unvisited_neighbors.append(next_word)
                    unvisited_words.remove(next_word)
        return unvisited_neighbors

    queue = deque([begin])
    unvisited_words.remove(begin)
    distance = 0

    while queue:  # while the queue is not empty
        level_size = len(queue)
        distance += 1

        for _ in range(level_size):
            current_word = queue.popleft()
            for neighbor in get_neighbors(current_word):
                if neighbor == end:
                    return distance
                queue.append(neighbor)
