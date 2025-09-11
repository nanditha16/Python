# There is an undirected graph with n nodes, where each node is numbered 
# between 0 and n - 1. You are given a 2D array graph, where graph[u] is 
# an array of nodes that node u is adjacent to. More formally, for each v
# in graph[u], there is an undirected edge between node u and node v. 
# The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v 
# such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent 
# sets A and B such that every edge in the graph connects a node in set A 
# and a node in set B.

# Return true if and only if it is bipartite.

# Constraints:
#     graph.length == n
#     1 <= n <= 100
#     0 <= graph[u].length < n
#     0 <= graph[u][i] <= n - 1
#     graph[u] does not contain u.
#     All the values of graph[u] are unique.
#     If graph[u] contains v, then graph[v] contains u.

# Time	O(V + E)	Each node and edge is visited once
# Space	O(V)	For color array and BFS queue
#     Where:
#     V = number of vertices (nodes)
#     E = number of edges

# Example:

# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent 
# sets such that every edge connects a node in one and a node in the other.

# Step-by-Step Explanation
# Initialize:
#     color[i] = -1 means node i is unvisited.
#     We use two colors: 0 and 1 to represent the two sets.
# Traverse each component:
#     For each unvisited node, start a BFS.
#     Assign color 0 to the starting node.
# BFS Coloring:
#     For each node, color its neighbors with the opposite color.
#     If a neighbor already has the same color → graph is not bipartite.
# Return Result:
#     If no conflicts are found, return True.

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means unvisited

        for start in range(n):
            if color[start] == -1:
                queue = deque([start])
                color[start] = 0  # Start coloring with 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False  # Same color on both ends of an edge
        return True
