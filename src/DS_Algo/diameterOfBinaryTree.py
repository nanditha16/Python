# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path 
# between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges
# between them.

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100

# Time Complexity: O(n)
#     Each node is visited once.
#     n is the number of nodes in the tree.
# Space Complexity: O(h)
#     h is the height of the tree (due to recursion stack).
#     Worst case (skewed tree): O(n)
#     Best case (balanced tree): O(log n)

# Example:
# Input: root = [1,2]
# Output: 1

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Step-by-Step Explanation
# Define a helper function depth(node):
    # Computes the depth (height) of the subtree rooted at node.
    # While computing depth, it also updates the maximum diameter.
# Diameter Calculation:
    # At each node, the longest path through that node is left_depth + right_depth.
    # Update self.max_diameter if this path is longer than the current maximum.
# Return the Result:
    # After traversing the entire tree, return self.max_diameter.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # Update diameter at this node
            self.max_diameter = max(self.max_diameter, left + right)
            # Return height of subtree
            return max(left, right) + 1

        depth(root)
        return self.max_diameter
