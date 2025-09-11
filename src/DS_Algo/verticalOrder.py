# Given the root of a binary tree, return the vertical order traversal of 
# its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from 
# left to right.

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Time	O(n)	Each node is visited once
# Space	O(n)	For queue and column table

# Example:
# Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
# Output: [[4],[2,5],[1,10,9,6],[3],[11]]

# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Step-by-Step Explanation
# Use BFS (Level Order Traversal):
#     Ensures nodes are processed top-to-bottom and left-to-right.
# Track Column Index:
#     Root starts at column 0.
#     Left child → column -1, right child → column +1.
# Store Nodes by Column:
#     Use defaultdict(list) to group node values by column index.
# Track Min/Max Column:
#     Helps in assembling the final result in correct left-to-right order.
# Return Result:
#     Extract values from column_table from min_col to max_col.

from typing import List, Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0)])  # (node, column)

        while queue:
            node, col = queue.popleft()
            column_table[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [column_table[x] for x in range(min_col, max_col + 1)]
