# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly
# linked list, the predecessor of the first element is the last element, 
# and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, 
# the left pointer of the tree node should point to its predecessor, 
# and the right pointer should point to its successor. You should 
# return the pointer to the smallest element of the linked list.

# Constraints:
    # The number of nodes in the tree is in the range [0, 2000].
    # -1000 <= Node.val <= 1000
    # All the values of the tree are unique.

# Time	O(n)	Each node is visited once
# Space	O(h)	Recursion stack, where h is the height of the tree
#         O(log n)	For balanced BST
#         O(n)	For skewed BST

# Example:

# Input: root = [2,1,3]
# Output: [1,2,3]

# Step-by-Step Explanation
# In-order Traversal:
#     Traverse the BST in sorted order (left → root → right).
#     This ensures nodes are visited in ascending order.
# Linking Nodes:
#     Maintain self.last to track the previously visited node.
#     Link self.last.right = current and current.left = self.last.
# Track Head and Tail:
#     self.first is set when visiting the smallest node (first in in-order).
#     self.last is updated at each step to the current node.
# Make the List Circular:
#     After traversal, link self.first.left = self.last and self.last.right = self.first.
# Return Head:
#     Return self.first as the head of the circular doubly linked list.

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None  # Edge case: empty tree

        self.first = None  # Head of the list
        self.last = None   # Tail of the list

        def inorder(node: Optional[Node]):
            if not node:
                return
            inorder(node.left)

            # Link current node with the last node in the list
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node  # First node (smallest)

            self.last = node  # Move last to current

            inorder(node.right)

        inorder(root)

        # Make it circular
        self.first.left = self.last
        self.last.right = self.first

        return self.first
