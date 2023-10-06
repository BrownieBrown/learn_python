from collections import deque, defaultdict
from enum import Enum
from typing import List, Dict


def is_valid_course_schedule(n: int, prerequisites: List[List[int]]) -> bool:
    # Helper function to find the indegree of all nodes in the graph
    def find_indegree(graph: Dict[int, List[int]]) -> Dict[int, int]:
        indegree: Dict[int, int] = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    # Helper function to perform topological sort on the graph
    def topo_sort(graph: Dict[int, List[int]]) -> bool:
        result = []
        queue = deque()
        indegree = find_indegree(graph)

        # Adding nodes with indegree of 0 to the queue
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        # Process the queue
        while queue:
            node = queue.popleft()
            result.append(node)

            # Reduce indegree for each neighbor
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If the result length matches 'n', the graph is a DAG and thus valid
        return len(result) == n

    # Create an adjacency list representation of the graph
    graph: Dict[int, List[int]] = {course: [] for course in range(n)}
    for a, b in prerequisites:
        graph[b].append(a)

    return topo_sort(graph)


class State(Enum):
    TO_VISIT = 0
    VISITING = 1
    VISITED = 2


def is_valid_course_schedule_dfs(n: int, prerequisites: List[List[int]]) -> bool:
    def build_graph():
        graph = defaultdict(list)
        for src, dest in prerequisites:
            graph[src].append(dest)
        return graph

    def dfs(start, states):
        # mark self as visiting
        states[start] = State.VISITINGx

        for next_vertex in graph[start]:
            # ignore visited nodes
            if states[next_vertex] == State.VISITED:
                continue

            # revisiting a visiting node, CYCLE!
            if states[next_vertex] == State.VISITING:
                return False

            # recursively visit neighbours
            # if a neighbour found a cycle, we return False right away
            if not dfs(next_vertex, states):
                return False

        # mark self as visited
        states[start] = State.VISITED

        # if we have gotten this far, our neighbours haven't found any cycle, return True
        return True

    graph = build_graph()
    states = [State.TO_VISIT for _ in range(n)]

    # dfs on each node
    for i in range(n):
        if not dfs(i, states):
            return False

    return True
