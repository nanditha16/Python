# Implement the BSTIterator class that represents an iterator over
#  the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
# The root of the BST is given as part of the constructor. The pointer should 
# be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal 
# to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, 
# the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, 
# there will be at least a next number in the in-order traversal when next()
#  is called.

# Follow up:
# Could you implement next() and hasNext() to run in average O(1)
#  time and use O(h) memory, where h is the height of the tree?

# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.

# Example:

# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False

# Method 1: Stack-Based In-Order Traversal

# How It Works
# 1. Initialization: Pushes the leftmost path from the root to the stack. This ensures the smallest element is on top.
# 2. next():
#     Pops the top node (current smallest).
#     If the node has a right child, pushes all its left descendants to the stack.
# 3. hasNext(): Checks if there are more nodes to visit by checking the stack.

# Time Complexity	O(1) amortized per next()
# Space Complexity	O(h) — height of tree
# Initialization Time	O(h) — leftmost path only

#  Key Advantages:
#     Lazy traversal: Only processes nodes as needed.
#     Efficient memory usage: Stores only part of the tree.
#     Fast initialization: No need to traverse the entire tree upfront.
#     Supports dynamic trees: Can be extended to handle updates.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)  # Initialize with leftmost path (smallest values)

    def _push_left(self, node):
        # Push all left children to the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the top node (next smallest value)
        node = self.stack.pop()
        # If the node has a right child, push its leftmost path
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        # If stack is not empty, there are more nodes to visit
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()