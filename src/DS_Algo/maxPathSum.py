
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
# in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass 
# through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.


# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000

# Time: O(n) — each node is visited once.
# Space: O(h) — recursion stack, where h is the height of the tree.

# Examples: 
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Explanation: 
# To solve the problem of finding the maximum path sum in a binary tree,
# where a path can start and end at any node,
# we use a recursive depth-first search (DFS) approach.
# For each node:
#     Compute the maximum gain from its left and right subtrees.
#     The maximum path sum at that node is:
#     node.val + left_gain + right_gain
#     Update a global variable to track the maximum path sum seen so far.
#     Return to the parent only the maximum gain from one side (left or right),
#     because a path can't split when going upward.

# Step-by-Step Execution
#     Let’s say the tree is:
#        -10
#        /  \
#       9   20
#           / \
#          15  7
# Step 1: Start DFS from root -10
#     Traverse left subtree → node 9
#     dfs(9) returns 9 (no children)
#     Traverse right subtree → node 20
#     Traverse left → dfs(15) returns 15
#     Traverse right → dfs(7) returns 7
#     current_sum = 20 + 15 + 7 = 42
#     Update self.max_path_sum = 42
#     Return 20 + max(15, 7) = 35 to parent
# Step 2: Back at root -10
#     left_gain = 9, right_gain = 35
#     current_sum = -10 + 9 + 35 = 34
#     self.max_path_sum remains 42 (since 34 < 42)
#     Return -10 + max(9, 35) = 25 (not used further)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')  # Tracks the highest path sum found

        def dfs(current_node):
            if not current_node:
                return 0

            # Recursively compute max gain from left and right subtrees
            left_gain = max(dfs(current_node.left), 0)   # Ignore negative paths
            right_gain = max(dfs(current_node.right), 0)

            # Path sum including current node and both children
            current_sum = current_node.val + left_gain + right_gain

            # Update global max if this path is better
            self.max_path_sum = max(self.max_path_sum, current_sum)

            # Return max gain to parent (only one side can be chosen)
            return current_node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_path_sum

