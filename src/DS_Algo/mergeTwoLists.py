# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example: 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Time Complexity: O(n+m) where n and m are the lengths of list1 and list2.
# Space Complexity: O(1) (in-place merge using existing nodes, no extra space except dummy node).

# Explanation
#     Create a dummy node to simplify list construction.
#     Use a pointer current to build the merged list.
#     Traverse both lists:
#         Compare current nodes.
#         Append the smaller one to the result.
#         Move the pointer forward.
#     After the loop, one list may still have remaining nodes.
#         Attach the rest directly since it's already sorted.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Convert a Python list to a linked list
    def list_to_linked_list(self, lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Convert a linked list back to a Python list
    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify result list construction
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining part of the non-empty list
        current.next = list1 if list1 else list2

        return dummy.next


# Create input lists
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# Merge the lists
solution = Solution()

# Convert to linked lists
l1 = solution.list_to_linked_list(list1)
l2 = solution.list_to_linked_list(list2)

merged_head = solution.mergeTwoLists(l1, l2)

# Convert result back to Python list
merged_list = solution.linked_list_to_list(merged_head)
print(merged_list)  # Output: [1, 1, 2, 3, 4, 4]
