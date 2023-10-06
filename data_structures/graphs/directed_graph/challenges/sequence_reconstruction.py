from collections import deque
from typing import List


def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    # Helper function to find indegree for each node in the graph
    def find_indegree(graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    # Perform topological sort and validate sequence reconstruction
    def topo_sort(graph):
        result = []
        queue = deque()
        indegree = find_indegree(graph)

        # Add nodes with indegree 0 to the queue
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        # Process nodes in queue
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            result.append(node)

            # Decrease indegree for neighboring nodes
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Validate sequence reconstruction
        return result == original

    # Build graph from sequences
    n = len(original)
    graph = {node: set() for node in range(1, 1 + n)}
    for seq in seqs:
        for i in range(len(seq) - 1):
            source, destination = seq[i], seq[i + 1]
            graph[source].add(destination)

    # Perform topological sort
    return topo_sort(graph)
