# Given the root of a binary search tree and a target value, 
# return the value in the BST that is closest to the target.
#  If there are multiple answers, print the smallest.

# Example:
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Input: root = [1], target = 4.428571
# Output: 1

# Constraints:
#     The number of nodes in the tree is in the range [1, 10^4].
#     0 <= Node.val <= 10^9
#     -10^9 <= target <= 10^9

# Edge Case Handling
#     Single node tree: Returns the only node value.
#     Target outside range: Still finds the closest value.
#     Multiple equally close values: Returns the smallest one as required.
#     Negative or large target values: Handled correctly due to float comparison.

# Step-by-Step Explanation
# Let’s walk through the example:
# PythonInput: root = [4,2,5,1,3], target = 3.714286
# Step 1: Initialize
#     closest = root.val = 4
# Step 2: Traverse the BST
# Compare abs(root.val - target) with abs(closest - target)
#     If closer, update closest
#     If equally close, choose the smaller value
#     Move left or right based on comparison between target and root.val
# Traversal Path:
#     Start at 4 → abs(4 - 3.714286) = 0.285714
#     Move left to 2 → abs(2 - 3.714286) = 1.714286 → not closer
#     Move right to 3 → abs(3 - 3.714286) = 0.714286 → not closer
#     Done → return 4

# Time Complexity
#     O(h) where h is the height of the tree
#     Worst case: O(n) (skewed tree)
#     Best case: O(logn) (balanced tree)
# Space Complexity
#     O(1) — iterative approach uses constant space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            # Update closest if current node is closer to target
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target):
                # If equally close, choose the smaller one
                closest = min(closest, root.val)

            # Move left or right depending on target
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest
