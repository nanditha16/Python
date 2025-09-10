# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Example:
# Input: root = [1,null,3]
# Output: [1,3]

# Input: root = []
# Output: []

# Explanation:
# To solve the right side view of a binary tree problem, 
# we need to return the list of node values that are visible when
# looking at the tree from the right side — top to bottom.
# Level Order Traversal (BFS)
#     We use Breadth-First Search (BFS) to traverse the tree level by level. 
# At each level, the last node we encounter is the one visible from the right side.

# How It Works (Step-by-Step)
# Method 1: BFS (Level Order Traversal)
#     Use a queue to traverse the tree level by level.
#     At each level, track the number of nodes (level_size).
#     For each node in the level:
#     Add its children to the queue.
#     If it's the last node in the level, add its value to the result.

# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(w) — where w is the maximum width of the tree (nodes at the widest level).

# Method 2: Recursive DFS (Right-first)
#     Traverse the tree using DFS, visiting right children first.
#     Track the current depth.
#     If it's the first time visiting this depth, add the node's value to the result.

# Time: O(n)
# Space: O(h) — recursion stack, h is height of tree. (can hit stack limit for deep trees)

# Method 3: Iterative DFS (Right-first using stack)
#     Use a stack to simulate DFS.
#     Push right child before left child so right is processed first.
#     Track depth and add the first node seen at each depth.

# Time: O(n)
# Space: O(h) — stack size

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    # Method 1: BFS (Level Order Traversal)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node in the current level, add to result
                if i == level_size - 1:
                    result.append(node.val)

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    # Method 2: Recursive DFS (right-first)
    def rightSideViewRecursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):          # first node seen at this depth
                res.append(node.val)
            dfs(node.right, depth + 1)     # go right first
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
    
    # Method 2: Iterative DFS (stack, right-first)
    def rightSideViewIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root, 0)]  # (node, depth)
        while stack:
            node, depth = stack.pop()
            if depth == len(res):          # first time we reach this depth
                res.append(node.val)
            # push left first so right is processed first (LIFO stack)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return res