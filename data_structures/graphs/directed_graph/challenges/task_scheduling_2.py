from collections import deque
from typing import List, Dict


def task_scheduling_2(tasks: List[str], times: List[int], requirements: List[List[str]]) -> int:
    # Helper function to calculate the indegree of all nodes
    def find_indegree(graph: Dict[str, List[str]]) -> Dict[str, int]:
        indegree: Dict[str, int] = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    # Function to perform topological sorting and calculate the minimum time needed
    def topo_sort(graph: Dict[str, List[str]], task_times: Dict[str, int]) -> int:
        queue: deque = deque()
        indegree: Dict[str, int] = find_indegree(graph)
        min_time: int = 0
        # Initialize the distance (time needed) from the source for each task
        distance: Dict[str, int] = {node: 0 for node in graph}

        # Populate initial queue and set initial time for tasks with indegree 0
        for node, degree in indegree.items():
            if degree == 0:
                queue.append(node)
                distance[node] = task_times[node]
                min_time = max(min_time, distance[node])

        # Process the queue
        while queue:
            node = queue.popleft()
            # Update indegree and distance (time needed) for all neighbors
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                distance[neighbor] = max(distance[neighbor], distance[node] + task_times[neighbor])
                min_time = max(min_time, distance[neighbor])

                # If indegree becomes zero, add neighbor to queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return min_time

    # Initialize the graph and task times from the inputs
    graph: Dict[str, List[str]] = {task: [] for task in tasks}
    task_times: Dict[str, int] = {tasks[i]: times[i] for i in range(len(tasks))}

    # Populate the graph based on requirements
    for a, b in requirements:
        graph[a].append(b)

    return topo_sort(graph, task_times)
