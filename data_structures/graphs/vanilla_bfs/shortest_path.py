from collections import deque
from typing import List


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    queue = deque([(a, 0)])  # Store the current node along with its depth
    visited = set()

    while queue:
        node, depth = queue.popleft()

        # Mark the node as visited
        visited.add(node)

        if node == b:
            return depth

        for neighbor in graph[node]:
            if neighbor not in visited:
                # Add the neighbor to the queue and mark it as visited
                queue.append((neighbor, depth + 1))
                visited.add(neighbor)

    return -1  # Return -1 if there's no path from 'a' to 'b'


def shortest_path_alternative(graph: List[List[int]], a: int, b: int) -> int:
    def get_neighbors(node: int):
        return graph[node]

    # BFS template
    def bfs(root: int, target: int):
        queue = deque([root])
        visited = {root}
        level = 0
        while queue:
            n = len(queue)
            for n in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1

    return bfs(a, b)
