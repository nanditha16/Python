# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.

# Example:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6

# Input: lists = []
# Output: []

# Input: lists = [[]]
# Output: []

# Method 1: Using Min-Heap
# Step-by-Step Explanation
# 1. Use a Min-Heap:
#     Store tuples of (node value, list index, node) to maintain order and avoid comparison errors between ListNode objects.
# 2. Initialize the Heap:
#     Push the head of each non-empty list into the heap.
# 3. Build the Result List:
#     Pop the smallest node from the heap.
#     Append it to the result list.
#     If the popped node has a next, push it into the heap.
# 4. Return the Merged List:
#     The dummy node helps simplify list construction.

# Edge Case Coverage
#     lists = [] → returns None
#     lists = [[]] → returns None
#     Lists with duplicate values → handled correctly
#     Lists with varying lengths → handled correctly

# Time Complexity: O(N log k)
#     N = total number of nodes across all lists
#     k = number of linked lists
#     Each node is pushed and popped from the heap once → O(log k) per operation
# Space Complexity: O(k) The heap stores at most k nodes at any time

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    # For easier testing and visualization
    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Step 1: Initialize the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # (value, index, node)

        dummy = ListNode(0)
        current = dummy

        # Step 2: Extract the smallest node and push its next into the heap
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
