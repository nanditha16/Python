
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
# so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:
#     It is the empty string, contains only lowercase characters, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.
    

# Example:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either '(' , ')', or lowercase English letter.

# Time Complexity: O(n)
#     One pass to identify invalid parentheses.
#     One pass to build the result string.
# Space Complexity: O(n)
#     Stack and to_remove set can grow up to size of input in worst case.
#     Result list also takes up to O(n) space.

# Step-by-Step Explanation
# Track unmatched parentheses:
#     Use a stack to store indices of '('.
#     When encountering ')', pop from the stack if there's a matching '(';
#      otherwise, mark it for removal.
# Mark unmatched '(':
#     After processing the string, any '(' left in the stack is unmatched and should be removed.
# Build the valid string:
#     Iterate through the original string and skip characters at indices marked for removal.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Step 1: Use a stack to track indices of unmatched '('
        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # matched with a previous '('
                else:
                    to_remove.add(i)  # unmatched ')'

        # Step 2: Add remaining unmatched '(' indices to removal set
        to_remove.update(stack)

        # Step 3: Build the result string excluding indices in to_remove
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)

        return ''.join(result)
