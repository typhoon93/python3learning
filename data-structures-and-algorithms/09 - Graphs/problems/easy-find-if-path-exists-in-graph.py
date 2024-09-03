"""

https://leetcode.com/problems/find-if-path-exists-in-graph


There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.



Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.


Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""
import collections


class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        """
        My solution; n param is not used in my solution, but can be used if you want to create the adjecancy graphs
        vertices before that.
        My solution is basically inspired by the Fluent Python book I am reading, relying on set operations.

        TC - O(E + V)
        SC - O(E + V)
        e = edges, v = vertices
        """
        # Check if the source is the same as the destination; trivially true if so
        if source == destination:
            return True

        # Creating an adjacency list to represent the graph (TC: O(E), SC: O(E + V))
        adjecancy_graph = collections.defaultdict(set)
        for v1, v2 in edges:
            adjecancy_graph[v1].add(v2)
            adjecancy_graph[v2].add(v1)

        # Initialize sets to store forward reachable paths and backward reachable paths (SC: O(V) for each)

        forward_paths = adjecancy_graph[source]
        backward_paths = adjecancy_graph[destination]  # all possible direct paths that lead to destination
        checked_paths = set()  # Set to keep track of visited nodes (SC: O(V))

        # Loop to explore the graph until no new vertices can be reached (TC for loop: O(E + V))
        while forward_paths:
            # Check if there is an intersection (TC: O(min(len(forward_paths), len(backward_paths)))
            if backward_paths & forward_paths:
                return True
            checked_paths |= forward_paths  # Add current forward_paths to visited (TC: O(len(forward_paths)), SC: O(len(forward_paths)))

            # TC: O(number of edges in forward_paths)
            forward_paths = {connection for vertex in forward_paths for connection in adjecancy_graph[vertex] if
                             connection not in checked_paths}
        return False

    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        """
        GPT solution, i just explored this. I belive i could have come up with this solution as well, if i took this road,
        as I am familiar with BFS algo

        In this approach we are traversing through the whole graph that can be reached from source, until we find destination, or
        the traversal is over.

        Time Complexity: O(E + V) - Each node and edge is processed once.
        Space Complexity: O(E + V) - Storing the graph and BFS queue.
        """

        if source == destination:
            return True

        adjacency_graph = collections.defaultdict(set)
        for v1, v2 in edges:
            adjacency_graph[v1].add(v2)
            adjacency_graph[v2].add(v1)

        visited = set()
        queue = collections.deque([source])

        while queue:

            current = queue.popleft()
            if current == destination:
                return True

            if current not in visited:
                visited.add(current)

                for neighbor in adjacency_graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return False



if __name__ == "__main__":
    sol = Solution()
    # n = 3
    # edges = [[0, 1], [1, 2], [2, 0]]
    # source = 0
    # destination = 2
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5

    print(sol.validPath(n, edges, source, destination))
