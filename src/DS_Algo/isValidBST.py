
# Given the root of a binary tree, determine if it is a valid binary search 
# tree (BST).

# A valid BST is defined as follows:
#     The left subtree of a node contains only nodes with keys strictly less than the node's key.
#     The right subtree of a node contains only nodes with keys strictly greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -2^31 <= Node.val <= 2^31 - 1

# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(h) — where h is the height of the tree (due to recursion stack).

# Example:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Input: root = [2,1,3]
# Output: true

# Explanation
# To determine if a binary tree is a valid Binary Search Tree (BST), we need to ensure that:
    # All nodes in the left subtree of a node have values strictly less than the node's value.
    # All nodes in the right subtree of a node have values strictly greater than the node's value.
    # Both subtrees must also be valid BSTs.
# The validate function checks whether each node's value is within a valid range:
    # For left children: value < parent.val
    # For right children: value > parent.val
# It recursively updates the bounds (low, high) as it traverses the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
      
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            # Left subtree must be < node.val
            if not validate(node.left, low, node.val):
                return False
            # Right subtree must be > node.val
            if not validate(node.right, node.val, high):
                return False
            return True  
        return validate(root)

# Example 1: Invalid BST
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

solution = Solution()
print(solution.isValidBST(root))  # Output: False

# Example 2: Valid BST
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

print(solution.isValidBST(root2))  # Output: True
