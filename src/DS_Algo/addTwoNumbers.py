# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Time Complexity: O(max(n,m)) where n and m are the lengths of l1 and l2.
# Space Complexity: O(max(n,m)) for the result linked list.
    
# Explanation
#     Each node in the linked list contains a single digit. 
#     Since the digits are stored in reverse order, the least significant digit comes first.
#     We simulate the addition digit by digit, just like how we do it manually, keeping track of the carry.


# Step-by-Step Example
# Input:
# l1 = [2,4,3] → represents 342
# l2 = [5,6,4] → represents 465

# Process:

# 2 + 5 = 7 → [7]
# 4 + 6 = 10 → carry = 1, digit = 0 → [7,0]
# 3 + 4 + 1 = 8 → [7,0,8]
# Output: [7,0,8] → represents 807

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
        for num in lst:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    # Convert a linked list back to a Python list
    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result  

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify result list construction
        dummy_head = ListNode(0)
        current_node = dummy_head

        # Initialize pointers to traverse the input lists
        pointer1 = l1
        pointer2 = l2

        # Variable to store carry from digit addition
        carry = 0

        # Loop until both lists are fully traversed and no carry remains
        while pointer1 or pointer2 or carry:
            # Get current values or 0 if the pointer is None
            value1 = pointer1.val if pointer1 else 0
            value2 = pointer2.val if pointer2 else 0

            # Calculate the sum and update carry using divmod
            carry, digit = divmod(value1 + value2 + carry, 10)

            # Create a new node with the digit and attach to result list
            current_node.next = ListNode(digit)
            current_node = current_node.next

            # Move to the next nodes in the input lists if available
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
        # Return the head of the resulting linked list
        return dummy_head.next


# Call the function
solution = Solution()

# Input lists
l1_list = [2, 4, 3]  # Represents 342
l2_list = [5, 6, 4]  # Represents 465

# Convert to linked lists
l1 = solution.list_to_linked_list(l1_list)
l2 = solution.list_to_linked_list(l2_list)

result_node = solution.addTwoNumbers(l1, l2)

# Convert result back to list
result_list = solution.linked_list_to_list(result_node)
print(result_list)  # Output: [7, 0, 8]
