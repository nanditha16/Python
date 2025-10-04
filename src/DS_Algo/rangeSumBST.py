# Given the root node of a binary search tree and two integers low and high,
#  return the sum of values of all nodes with a value in the inclusive 
#  range [low, high].

# Example:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 
# Constraints:
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.

# Method 1: Recursive
Step-by-Step Explanation
Step 1: Traverse the tree recursively
Step 2: Sum the included values

# Edge Case Handling
#     Empty tree: Returns 0 safely.
#     All nodes out of range: Skips unnecessary branches.
#     Single node tree: Correctly returns the node value if in range.
#     Large trees: Efficient due to BST pruning.

# Time Complexity
#     Best case (balanced BST with pruning):O(logn)
#     Worst case (unbalanced BST or all nodes in range): O(n)

# Space Complexity
#     Recursive stack: O(h) where hhh is the height of the tree
#     Worst case: O(n)(skewed tree)
#     Best case: O(logn) (balanced tree)

# Method 2: Iterative

# # Step-by-Step Explanation
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Step 1: Initialize
#     res = 0
#     stack = [root] → starts with node 10
# Step 2: Traverse Iteratively
#     Pop 10 → in range → res = 10
#     10 >= low → push left (5)
#     10 <= high → push right (15)
#     Pop 15 → in range → res = 25
#     15 >= low → push left (None)
#     15 <= high → push right (18)
#     Pop 18 → out of range (> high) → skip right, push left (None)
#     Pop None → skip
#     Pop 5 → out of range (< low) → skip left, push right (7)
#     Pop 7 → in range → res = 32
#     Push left (None) and right (None)
#     Remaining Nones → skipped
#     Final Result: res = 32

# Edge Case Handling
#     Empty tree: stack = [None] → safely handled by if node: check.
#     Single node tree: Works correctly if the node is in range.
#     All nodes out of range: Efficiently skips unnecessary branches.
#     Large trees: Avoids recursion depth issues.

# Time Complexity
#     Best case (pruned traversal): O(logn)
#     Worst case (all nodes visited): O(n)

# Space Complexity
#     Stack size: up to O(h)) where hhh is tree height
#     Worst case: O(n) (skewed tree)
#     Best case: O(logn) (balanced tree)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBSTRecursive(self, root: Optional[TreeNode], low: int, high: int) -> int:
       # Base case: if the node is None, return 0
        if not root:
            return 0

        # If the node's value is less than low, skip the left subtree
        if root.val < low:
            return self.rangeSumBSTRecursive(root.right, low, high)

        # If the node's value is greater than high, skip the right subtree
        if root.val > high:
            return self.rangeSumBSTRecursive(root.left, low, high)

        # If the node's value is within range, include it and recurse both sides
        return (root.val +
                self.rangeSumBSTRecursive(root.left, low, high) +
                self.rangeSumBSTRecursive(root.right, low, high))

    def rangeSumBSTIterative(self, root: TreeNode, low: int, high: int) -> int:
        res = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue

            if low <= node.val <= high:
                res += node.val
            if node.val > low:   # only then left can have in-range values
                stack.append(node.left)
            if node.val < high:  # only then right can have in-range values
                stack.append(node.right)

        return res
