from collections import deque
from typing import List, Optional


def find_indegree(graph):
    """Calculate the indegree of all nodes in the graph."""
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree


def topo_sort(graph):
    """Perform topological sorting on the graph."""
    result = []
    queue = deque()
    indegree = find_indegree(graph)

    # Add nodes with indegree 0 to the queue
    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        result.append(node)

        # Update indegree for neighbors
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If topological sorting is not possible, return None
    return result if len(graph) == len(result) else None


def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> Optional[List[str]]:
    """Schedule tasks based on their requirements using topological sorting."""
    graph = {t: [] for t in tasks}

    # Create the graph based on requirements
    for a, b in requirements:
        graph[a].append(b)

    return topo_sort(graph)
