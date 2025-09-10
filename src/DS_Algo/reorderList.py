# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Constraints:
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

# Time Complexity: O(n)
#     Finding the middle of the list takes O(n/2) → O(n)
#     Reversing the second half takes O(n/2) → O(n)
#     Merging the two halves takes O(n)
#     So overall, the function performs three linear passes over the list:
#     O(n) + O(n) + O(n) = O(n)

# Space Complexity: O(1)
#     The algorithm uses only a few pointers (slow, fast, prev, temp, etc.)
#     No additional data structures are used.
#     The reordering is done in-place, modifying the next pointers of the existing nodes.

# Example:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Explanation:
# three-step approach
# 1. Find the middle of the list
#     Use the slow and fast pointer technique to find the midpoint.
# 2. Reverse the second half
#     Reverse the second half of the list starting from the middle.
# 3. Merge the two halves
#     Interleave nodes from the first and reversed second half.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
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
    def linked_list_to_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Reorders the linked list in-place to follow the pattern:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second = slow.next
        prev = None
        slow.next = None  # Split the list into two halves
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

# Create input list
input_list = [1, 2, 3, 4, 5]

# Reorder the list
solution = Solution()
head = solution.list_to_linked_list(input_list)
solution.reorderList(head)

# Convert back to Python list and print
output_list = solution.linked_list_to_list(head)
print(output_list)  # Output: [1, 5, 2, 4, 3]
      