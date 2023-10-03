from collections import deque
from typing import List


def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    # Pre-calculate the next and previous digits for each digit.
    next_digit = {str(i): str(i + 1) for i in range(9)}
    next_digit["9"] = "0"
    prev_digit = {v: k for k, v in next_digit.items()}

    # Check for a trivial case where target_combo is the initial state.
    if target_combo == "0000":
        return 0

    # Convert the list of trapped_combos to a set for O(1) lookups.
    trapped_combo_set = set(trapped_combos)

    # Initialize steps dictionary with initial state and a BFS queue.
    steps = {"0000": 0}
    bfs_queue = deque(["0000"])

    # Perform BFS to find the shortest path to the target_combo.
    while bfs_queue:
        current_combo = bfs_queue.popleft()

        # Generate the next states by rotating each wheel forward and backward.
        for i in range(4):
            for d in [next_digit, prev_digit]:
                new_combo = current_combo[:i] + d[current_combo[i]] + current_combo[i + 1:]

                # If the new_combo is not trapped and hasn't been visited yet.
                if new_combo not in trapped_combo_set and new_combo not in steps:
                    # Update the steps needed to reach new_combo and enqueue it for BFS.
                    steps[new_combo] = steps[current_combo] + 1
                    bfs_queue.append(new_combo)

                    # If the new_combo matches the target_combo, return the number of steps.
                    if new_combo == target_combo:
                        return steps[new_combo]

    # If we can't reach the target_combo, return -1.
    return -1
