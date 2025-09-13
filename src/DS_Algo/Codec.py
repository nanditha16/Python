# Serialization is the process of converting a data structure or object 
# into a sequence of bits so that it can be stored in a file or memory buffer,
#  or transmitted across a network connection link to be reconstructed later
#   in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization
#  algorithm should work. You just need to ensure that a binary tree 
#  can be serialized to a string and this string can be deserialized to
#   the original tree structure.

# Clarification: The input/output format is the same as how LeetCode 
# serializes a binary tree. You do not necessarily need to follow this format,
#  so please be creative and come up with different approaches yourself.

# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000

# Example:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Input: root = []
# Output: []

# Method 1: using preorder traversal with null markers. 

# Step-by-Step Explanation
# 1. Serialization
#     1. Start from the root node.
#     2. Traverse the tree in preorder: root → left → right.
#     3. For each node:
#         If it's None, append "null" to the result.
#         Otherwise, append its value.
#     4. Convert the list of values into a comma-separated string.
# 2. Deserialization
#     1. Split the serialized string into a list of values.
#     2. Use an iterator to process values one by one.
#     3. For each value:
#         If it's "null", return None.
#         Otherwise, create a TreeNode with the value.
#     4. Recursively build the left and right subtrees.

# Example
# For a tree like:
#     1
#    / \
#   2   3
#      / \
#     4   5
# Serialized output: "1,2,null,null,3,4,null,null,5,null,null"

# Serialization
#     Time Complexity: O(n) Each node is visited once.
#     Space Complexity: O(n) Output list + recursion stack.
# Deserialization
#     Time Complexity: O(n) Each value is processed once.
#     Space Complexity: O(n) Recursion stack + tree nodes.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a binary tree to a single string using preorder traversal.
        Each node is visited in the order: root -> left -> right.
        Null children are represented by the string "null".
        """
        def dfs(node):
            if not node:
                vals.append("null")  # Use "null" to mark missing children
                return
            vals.append(str(node.val))  # Add current node's value
            dfs(node.left)              # Recurse on left child
            dfs(node.right)             # Recurse on right child
        
        vals = []
        dfs(root)
        return ','.join(vals)  # Join all values into a single comma-separated string

    def deserialize(self, data):
        """
        Decodes the serialized string back into the original binary tree.
        Uses preorder traversal to reconstruct the tree.
        """
        def dfs():
            val = next(vals)  # Get the next value from the iterator
            if val == "null":
                return None   # If it's "null", return None (no node)
            node = TreeNode(int(val))  # Create a node with the value
            node.left = dfs()          # Reconstruct left subtree
            node.right = dfs()         # Reconstruct right subtree
            return node
        
        vals = iter(data.split(','))  # Convert string back to list and make it iterable
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))