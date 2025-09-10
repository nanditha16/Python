# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child 
# pointer points to the next node in the list and the left child pointer 
# is always null.
# The "linked list" should be in the same order as a pre-order traversal 
# of the binary tree.

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Time Complexity	O(n) — each node is visited once
# Space Complexity	O(1) — no recursion or stack used

# Example:
# Input: root = [0]
# Output: [0]

# Input: root = []
# Output: []

# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# To flatten a binary tree into a linked list in-place,
#  where each node's right child points to the next node 
# in pre-order traversal and the left child is always None,
# you can use a recursive or iterative approach.

# This is a Morris traversal-inspired approach:
    # For each node, if it has a left child:
        # Find the rightmost node in the left subtree.
        # Attach the current node’s right subtree to that node’s right.
        # Move the left subtree to the right.
        # Set the left to None.
    # Move to the next node via right.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

from typing import Optional

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens the binary tree to a linked list in-place using pre-order traversal.
        """
        current = root
        while current:
            if current.left:
                # Find the rightmost node of the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right

                # Rewire the connections
                rightmost.right = current.right
                current.right = current.left
                current.left = None

            # Move to the next node
            current = current.right

