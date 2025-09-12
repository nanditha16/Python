# You are given a nested list of integers nestedList. 
# Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. 
# For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

# Example :
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

# Input: nestedList = [0]
# Output: 0
 
# Constraints:
# 1 <= nestedList.length <= 50
# The values of the integers in the nested list is in the range [-100, 100].
# The maximum depth of any integer is less than or equal to 50.

# Method 1: Recursive DFS (Depth-First Search) 
# Step-by-Step Explanation
# 1. Recursive DFS (Depth-First Search) is used to traverse the nested structure.
# 2. For each element:
#     If it's an integer, multiply it by its depth and add to the total.
#     If it's a list, recursively call the function with increased depth.
# 3. Start with depth = 1 for the outermost list.

# Time Complexity: O(n)
#     Where n is the total number of integers and lists in the structure. 
#     Each element is visited once.
# Space Complexity: O(d)
#     Where d is the maximum depth of nesting due to recursive call stack.

# Method 2: Iterative solution using a queue (BFS approach) 
# Step-by-Step Explanation
# 1. We use a queue to process each level of nesting.
# 2. Each element in the queue is a tuple: (list, depth).
# 3. For each item:
#     - If it's an integer, multiply by its depth and add to total.
#     - If it's a list, enqueue it with depth incremented by 1.

# Time Complexity:  O(n) — each element is visited once.
# Space Complexity: O(n) — queue stores elements at each level.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


from typing import List
from collections import deque

class Solution:
    def depthSum_Recursive_DFS(self, nestedList: List[NestedInteger]) -> int:
       def dfs(nlist, depth):
            total = 0
            for item in nlist:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
    
    def depthSum_Iterative(self, nestedList: List['NestedInteger']) -> int:
        queue = deque([(nestedList, 1)])  # Each item is (list, depth)
        total = 0

        while queue:
            current_list, depth = queue.popleft()
            for item in current_list:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    queue.append((item.getList(), depth + 1))

        return total
