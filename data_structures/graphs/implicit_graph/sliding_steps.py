from collections import deque
from typing import List

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
target = ((1, 2, 3), (4, 5, 0))
max_row = 2
max_col = 3


def num_steps(init_pos: List[List[int]]) -> int:
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0

    # Dictionary to maintain steps to reach a particular state
    moves_map = {init_pos: 0}

    # Queue for BFS
    moves_queue = deque([init_pos])

    while moves_queue:
        current_state = moves_queue.popleft()

        # Finding the position of zero (empty spot)
        row, col = 0, 0
        for i, line in enumerate(current_state):
            for j, entry in enumerate(line):
                if entry == 0:
                    row, col = i, j

        # Checking each possible move
        for delta_row, delta_col in directions:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < max_row and 0 <= new_col < max_col:
                # Creating a new state after the move
                new_state = list(list(line) for line in current_state)
                new_state[new_row][new_col], new_state[row][col] = new_state[row][col], new_state[new_row][new_col]

                # Converting to tuple to make it hashable
                new_tuples = tuple(tuple(line) for line in new_state)

                # If this state has not been visited
                if new_tuples not in moves_map:
                    moves_map[new_tuples] = moves_map[current_state] + 1
                    moves_queue.append(new_tuples)
                    if new_tuples == target:
                        return moves_map[new_tuples]
    return -1
