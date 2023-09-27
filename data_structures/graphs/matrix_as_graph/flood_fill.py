from collections import deque
from typing import List


def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])
    original_pixel = image[r][c]

    def get_neighbors(coord):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        neighbors = []

        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]

            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                neighbors.append((neighbor_row, neighbor_col))

        return neighbors

    # Perform BFS
    def bfs(start_r, start_c):
        # Initialize the queue for BFS with the starting point
        queue = deque([(start_r, start_c)])

        while queue:
            row, col = queue.popleft()
            current_pixel = image[row][col]

            if current_pixel == original_pixel:
                image[row][col] = replacement

            for neighbor_row, neighbor_col in get_neighbors([row, col]):
                if image[neighbor_row][neighbor_col] == original_pixel:
                    queue.append((neighbor_row, neighbor_col))

    # Call the BFS helper function to perform the flood fill
    bfs(r, c)

    return image
