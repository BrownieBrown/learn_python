from collections import deque
from typing import List


def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    # Directions for possible moves (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Define the "INF" constant as the maximum integer value.
    INF = 2 ** 31 - 1

    # Initialize an empty queue for BFS and find the dimensions of the map.
    queue = deque()
    rows, cols = len(dungeon_map), len(dungeon_map[0])

    # Add all gates to the queue to seed the BFS.
    for i, row in enumerate(dungeon_map):
        for j, val in enumerate(row):
            if val == 0:
                queue.append((i, j))

    # Perform BFS starting from the gates to populate distances.
    while queue:
        cur_row, cur_col = queue.popleft()

        # Explore all four possible directions from the current cell.
        for delta_row, delta_col in directions:
            new_row, new_col = cur_row + delta_row, cur_col + delta_col

            # Check for valid boundary conditions.
            if 0 <= new_row < rows and 0 <= new_col < cols:

                # If the neighboring cell is "INF", it has not been visited yet.
                if dungeon_map[new_row][new_col] == INF:
                    # Update the distance of the neighboring cell.
                    dungeon_map[new_row][new_col] = dungeon_map[cur_row][cur_col] + 1

                    # Add the neighboring cell to the queue for further exploration.
                    queue.append((new_row, new_col))

    return dungeon_map
