from collections import deque


def find_indegree(graph):
    indegree = {node: 0 for node in graph}  # Initialize all indegrees to zero
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1  # Increment indegree for each neighbor
    return indegree


def topo_sort(graph):
    res = []
    q = deque()

    # Find the indegree of each node
    indegree = find_indegree(graph)

    # Add nodes with indegree 0 to the queue
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)

    while len(q) > 0:
        node = q.popleft()  # Remove a node with indegree 0
        res.append(node)  # Add it to the result

        # Decrease the indegree of all its neighbors
        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            # If indegree becomes zero, add to queue
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # If the length of the result is the same as graph, return result; otherwise, graph has a cycle
    return res if len(graph) == len(res) else None
