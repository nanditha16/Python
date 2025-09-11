# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both 
# p and q as descendants (where we allow a node to be a descendant of itself).”

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Time Complexity: O(n)
#     Each node is visited once.
#     n is the number of nodes in the tree.
# Space Complexity:
#     O(h) for recursion stack, where h is the height of the tree.
#     Worst case (skewed tree): O(n)
#     Best case (balanced tree): O(log n)

# Example:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Step-by-Step Explanation
# Base Case:
#     If the current node is None, return None.
#     If the current node is either p or q, return it (because a 
#     node is a descendant of itself).
# Recursive Search:
#     Search for p and q in the left and right subtrees.
# Decision Point:
#     If both left and right recursive calls return non-null, it means p
#         and q are found in different subtrees → current node is the LCA.
#     If only one side returns non-null, propagate that result upward.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or matches one of the nodes
        if root is None or root == p or root == q:
            return root

        # Recurse on left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return non-null, root is the LCA
        if left and right:
            return root

        # Otherwise, return the non-null side
        return left if left else right
