"""
https://leetcode.com/problems/find-center-of-star-graph/


There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.



Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1


Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
"""
import collections
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        My code
        O(n)
        """
        adjecancy_graph = collections.defaultdict(list)
        for edge1, edge2 in edges:
            adjecancy_graph[edge1].append(edge2)
            adjecancy_graph[edge2].append(edge1)
        for node, connections in adjecancy_graph.items():
            if len(connections) >= len(edges):
                return node
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        O(1), created after seeing other solutions. Assumption here is that every node connects to the center but not to any other node.
        So if a node gets 2 connections, we are golden and can return;
        I do not like the one liner solutions as they are unnecassarily unclear
        """
        connections_count = collections.defaultdict(int)
        for edge1, edge2 in edges[:2]:
            connections_count[edge1] += 1
            connections_count[edge2] += 1
            if connections_count[edge1] >= 2:
                return edge1
            if connections_count[edge2] >= 2:
                return edge2

        #one liner:
        #return edges[0][0] if edges[0][0] == edges[1][1] or edges[0][0] == edges[1][0] else edges[0][1]



if __name__ == "__main__":
    sol = Solution()
    edges = [[1, 2], [2, 3], [4, 2]]
    print(sol.findCenter(edges))
