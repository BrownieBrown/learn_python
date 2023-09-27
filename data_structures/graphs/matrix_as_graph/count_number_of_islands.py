from collections import deque
from typing import List, Tuple


def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    count = 0  # To keep track of the number of islands
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    def get_neighbors(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Returns all the valid neighbors of a given coordinate."""
        row, col = coord
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                neighbors.append((new_row, new_col))

        return neighbors

    def bfs(start: Tuple[int, int]):
        """Performs BFS starting from the coordinate 'start'."""
        queue = deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            curr_row, curr_col = queue.popleft()

            for neighbor_row, neighbor_col in get_neighbors((curr_row, curr_col)):
                if not visited[neighbor_row][neighbor_col] and grid[neighbor_row][neighbor_col] == 1:
                    queue.append((neighbor_row, neighbor_col))
                    visited[neighbor_row][neighbor_col] = True

    # Main loop to go through each cell in the grid
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1 and not visited[r][c]:
                bfs((r, c))
                count += 1  # Increment the island count

    return count
