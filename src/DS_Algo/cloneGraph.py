# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed).
# For example, the first node with val == 1, the second node with val == 2,
#  and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a 
# finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1.
#  You must return the copy of the given node as a reference to the cloned graph.

# Constraints:
#     The number of nodes in the graph is in the range [0, 100].
#     1 <= Node.val <= 100
#     Node.val is unique for each node.
#     There are no repeated edges and no self-loops in the graph.
#     The Graph is connected and all nodes can be visited starting from 
#   the given node.

# Time Complexity: O(N+E) where N is the number of nodes and E is the number of edges.
# Space Complexity: O(N) — for the visited dictionary and recursion stack.

# Example:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. 
# The graph consists of only one node with val = 1 and it does not 
# have any neighbors.

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Step-by-Step Explanation
# 1. Base case: If node is None, return None.
# 2. Use a dictionary visited to store already cloned nodes.
# 3. For each node:
#     If already cloned, return the clone.
#     Otherwise, create a new node with the same value.
#     Recursively clone all neighbors and add them to the clone’s neighbor list.
# 4. Return the clone of the starting node.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # Maps original node → cloned node

        def dfs(current):
            if current in visited:
                return visited[current]

            # Clone the current node
            clone = Node(current.val)
            visited[current] = clone

            # Recursively clone neighbors
            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
