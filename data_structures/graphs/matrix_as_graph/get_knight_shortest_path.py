from collections import deque
from typing import Tuple, List


def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(coords: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = coords
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        neighbors = [(row + dr, col + dc) for dr, dc in directions]

        return neighbors

    def bfs(start: Tuple[int, int], target: Tuple[int, int]) -> int:
        queue = deque([(start, 0)])  # Added the initial distance 0
        visited = {start}

        while queue:
            (current_row, current_col), distance = queue.popleft()  # distance added

            if (current_row, current_col) == target:
                return distance  # Return the distance to the target

            for neighbor in get_neighbors((current_row, current_col)):
                if neighbor in visited:
                    continue

                queue.append((neighbor, distance + 1))  # Increment the distance by 1
                visited.add(neighbor)

    return bfs((0, 0), (x, y))
