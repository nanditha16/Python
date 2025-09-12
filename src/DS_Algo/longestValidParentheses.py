
# Given a string containing just the characters '(' and ')', 
# return the length of the longest valid (well-formed) parentheses substring.

# Constraints:
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.

# Example:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Input: s = ""
# Output: 0

# Method 1:
#  Step-by-Step Explanation
# 1. Initialize a stack with -1:
#     This acts as a base for calculating lengths when valid substrings start at index 0.
# 2. Iterate through the string:
#     If '(', push its index onto the stack.
#     If ')', pop the top:
#         If the stack becomes empty, push the current index as a new base.
#         Otherwise, calculate the length of the current valid substring as i - stack[-1].
# 3. Track the maximum length throughout the iteration.

# Example Walkthrough
# Input: "(()"
# Stack: [-1]
# i = 0 → '(' → push → [-1, 0]
# i = 1 → '(' → push → [-1, 0, 1]
# i = 2 → ')' → pop → [-1, 0] → valid length = 2 - 0 = 2
# Output: 2

# Time Complexity: O(n) — single pass through the string.
# Space Complexity: O(n) — stack stores indices.

# Method 2: Dynamic Programming
# Step-by-Step Explanation
# 1. Create a DP array dp where dp[i] represents the length of the longest valid substring ending at index i.
# 2. Initialize all dp values to 0.
# 3. Iterate through the string starting from index 1:
#     If s[i] == ')':
#         Check the character before it:
#         - If s[i-1] == '(', then dp[i] = dp[i-2] + 2
#         - If s[i-1] == ')' and s[i - dp[i-1] - 1] == '(', then dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
# 4. Track the maximum value in dp array.           

# Step-by-Step Explanation
# 1. Initialize:
#     dp[i] stores the length of the longest valid substring ending at index i.
#     max_len keeps track of the maximum length found.
# 2. Iterate through the string:
#     consider positions where s[i] == ')' because valid substrings must end with a closing bracket.
# 3. Two main cases:
#     Case 1: If s[i-1] == '(', then we found a pair "()". Add 2 to the length of valid substring ending at i-2.
#     Case 2: If s[i-1] == ')', we check if the character before the previous valid substring (i - dp[i-1] - 1) is '('. If so, we add 2 plus the length of the valid substring before that.
# 4. Update max_len after each valid substring is found.

# Edge Case Handling
#     Empty string "" → returns 0
#     String with no valid pairs like "((((" or "))))" → returns 0
#     Mixed valid and invalid substrings like "()(()" → returns correct longest valid substring
#     Nested and consecutive valid substrings like "(()())" or "()()()" → handled correctly

# Time Complexity: O(n) We iterate through the string once.
# Space Complexity: O(n) We use a DP array of size n.

# Method 3: Two-pass counter approach (also known as the left-right scan method)
# Step-by-Step Explanation
# 1. Initialize two counters, left and right, to zero. These will count the number of '(' and ')' respectively.
# 2. First Pass (Left to Right):
#     Iterate through the string:
#     - For each '(', increment the left counter.
#     - For each ')', increment the right counter.
#     - Whenever left equals right, calculate the length of the valid substring (2 * right) and update max_len if it's greater.
#     - If right exceeds left, reset both counters to zero.
# 3. Second Pass (Right to Left):
#     Reset left and right counters to zero.
#     Iterate through the string in reverse:
#     - For each ')', increment the right counter.
#     - For each '(', increment the left counter.
#     - Whenever left equals right, calculate the length of the valid substring (2 * left) and update max_len if it's greater.
#     - If left exceeds right, reset both counters to zero.
# 4. Return max_len as the result.  

# Step-by-Step Explanation
# 1. First Pass (Left to Right):
#     Count left and right parentheses.
#     If left == right, we have a valid substring → update max_len.
#     If right > left, reset counters (invalid sequence).
# 2. Second Pass (Right to Left):
#     Same logic, but reversed:
#     Count right and left from the end.
#     If left == right, update max_len.
#     If left > right, reset counters.
# This second pass is necessary to catch cases like "(()" which would be missed in the left-to-right scan.

#  Edge Case Handling
#     Empty string "" → returns 0
#     Strings with no valid pairs like "((((" or "))))" → returns 0
#     Mixed valid and invalid substrings like "()(()" → returns correct longest valid substring
#     Handles nested and consecutive valid substrings like "(()())" or "()()()"

# Time Complexity: O(n) Two linear scans of the string.
# Space Complexity: O(1) Only counters are used, no extra space proportional to input size.

class Solution:
    # Method 1: Using a Stack
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize with -1 to handle edge cases
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # reset base index
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

    # Method 2: Dynamic Programming
    def longestValidParenthesesDP(self, s: str) -> int:
       n = len(s)
        if n < 2:
            return 0

        # dp[i] will store the length of the longest valid substring ending at index i
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                # Case 1: Substring ends with "()", so we check i-1
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                # Case 2: Substring ends with "))", check if there's a matching "("
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

                max_len = max(max_len, dp[i])

        return max_len

    #method 3: Two-pass counter approach (also known as the left-right scan method)
    def longestValidParenthesesTwoPassCounter(s: str) -> int:
        max_len = 0
        left = right = 0

        # Left to right scan
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left scan
        left = right = 0
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len
