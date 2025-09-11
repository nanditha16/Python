
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
        
# Example:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Input: root = [1]
# Output: ["1"]

# Method 1: Step-by-Step Explanation
# 1. Initialize an empty list paths to store all root-to-leaf paths.
# 2. Define a helper function dfs(node, path):
#     If the node is not None, append its value to the current path.
#     If it's a leaf node (no left or right children), add the path to paths.
#     Otherwise, recursively call dfs on left and right children, appending "->" to the path.
# 3. Start DFS from the root with an empty path.
# 4. Return the list of paths.

# Time: 
#     Each path += str(node.val) creates a new string (strings are immutable).
#     For a path of length L, you do ~L concatenations → O(L²) work per path.
#     Across P root-to-leaf paths: ~O(∑ Lᵢ²). In a skewed tree this can reach O(N²).
# Space: O(H) recursion stack (H = height) + result storage. 
#     Extra transient strings created along the way inflate constant factors.

# Method 2: the backtracking version that avoids repeated string concatenations by 
# using a list and join at leaves:

# Algorithm (DFS with backtracking)
# 1. Start with res = [], path = [].
# 2. DFS(node):
#     If node is None, return (dead end).
#     Choose: path.append(str(node.val)) (Now path represents the route to node.)
#     Leaf check: If node.left is None and node.right is None:
#         - Build the path string once: res.append("->".join(path))
#     Explore children:
#         dfs(node.left)
#         dfs(node.right)
#     Un-choose (backtrack): path.pop() - (Restore path to state before visiting node.)
# 3. Call dfs(root) and return res.

# Time: Appends/pops on the list are O(1). 
#     At each leaf, join costs O(L) once.
#     Across all paths: O(N + ∑ Lᵢ) = O(N + total_output_chars). 
#     (Much better overhead.)
# Space: O(H) for the call stack + O(H) for the path list + result storage.

# Tiny dry run
#   1
#    / \
#   2   3
#    \
#     5
# Start: path=[]
# Visit 1: path=['1']
#     Left → 2: path=['1','2']
#         Left → None (return)
#         Right → 5: path=['1','2','5'] (leaf) ⇒ add "1->2->5"
#         Backtrack to 2: path=['1','2'] → backtrack to 1: path=['1']
#     Right → 3: path=['1','3'] (leaf) ⇒ add "1->3"
#     Backtrack to 1: path=['1'] → backtrack to root: []
# Result: ["1->2->5", "1->3"]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional   
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(node: TreeNode, path: str):
            if node:
                path += str(node.val)
                # If it's a leaf, add the path to result
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, "")
        return paths
    
    def binaryTreePathsBacktracking(self, root: Optional[TreeNode]) -> List[str]:
        res: List[str] = []
        path: List[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            # choose
            path.append(str(node.val))

            # check leaf
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                # explore
                dfs(node.left)
                dfs(node.right)

            # un-choose (backtrack)
            path.pop()

        dfs(root)
        return res
 