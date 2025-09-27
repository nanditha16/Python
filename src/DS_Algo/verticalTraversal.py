# Given the root of a binary tree, calculate the vertical order traversal
#  of the binary tree.

# For each node at position (row, col), its left and right
#  children will be at positions (row + 1, col - 1) and 
# (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list
#  of top-to-bottom orderings for each column index starting 
# from the leftmost column and ending on the rightmost column. 
# There may be multiple nodes in the same row and same column. 
# In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

# Example:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order
#  from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.

# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0),
#            so we order them by their value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.

# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# This case is the exact same as example 2, but with nodes
#  5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same 
# location and should be ordered by their values.

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000

# Step-by-Step Explanation
# Step 1: BFS Traversal with Column and Row Tracking
#     We use a queue to perform Breadth-First Search (BFS) and track:
#     - column: horizontal position (left = -1, right = +1)
#     - row: vertical depth (root = 0, children = +1)

# Step 2: Collect Nodes with Position Info
#     As we traverse the tree, we collect each node's:
#     - Column index
#     - Row index
#     - Value
#     This gives us a list of tuples like:
# Step 3: Sort Nodes
#     We sort the list of nodes by:
#     - Column (left to right)
#     - Row (top to bottom)
#     - Value (ascending)
#     This ensures correct ordering even when multiple nodes share the
#      same column and row.
# Step 4: Group Nodes by Column
#     We use a dictionary to group node values by their column index:
#     After grouping, we get something like:
# Step 5: Build Final Output
#     We extract the values in order of increasing column index:

# Time Complexity:
#     BFS Traversal: O(n) — each node is visited once.
#     Sorting: O(nlogn) — sorting the list of nodes.
#     Grouping: O(n) — building the final result.
# Space Complexity:
#     Queue + node list + result dictionary:  O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # List to hold (col, row, val) for sorting
        nodes = []

        # BFS traversal with row and column tracking
        queue = deque([(root, 0, 0)])  # (node, col, row)

        while queue:
            node, col, row = queue.popleft()
            if node:
                nodes.append((col, row, node.val))
                queue.append((node.left, col - 1, row + 1))
                queue.append((node.right, col + 1, row + 1))

        # Sort by column, then row, then value
        nodes.sort()

        # Group by column
        result = defaultdict(list)
        for col, row, val in nodes:
            result[col].append(val)

        # Return results in column order
        return [result[x] for x in sorted(result)]

