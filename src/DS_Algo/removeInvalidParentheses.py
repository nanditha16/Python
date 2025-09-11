# Given a string s that contains parentheses and letters,
#  remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with 
# the minimum number of removals. You may return the answer in any order.

# Constraints:
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.

# Time	O(2ⁿ × n)	Worst-case: generate all substrings
# Space	O(2ⁿ)	For queue and visited set
# Where n is the length of the input string.

# Example:
# Input: s = "()())()"
# Output: ["(())()","()()()"]

# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]

# Input: s = ")("
# Output: [""]

# Step-by-Step Explanation
# Validation Function:
#     is_valid() checks if a string has balanced parentheses using a counter.
# Breadth-First Search (BFS):
#     Start with the original string.
#     At each level, remove one parenthesis and enqueue the new string.
#     Stop further exploration once valid strings are found at the current level (minimum removals).
# Avoid Duplicates:
#     Use a visited set to avoid reprocessing the same string.
# Return Result:
#     If no valid strings are found, return [""].

from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        visited = set()
        queue = deque([s])
        found = False
        result = []

        while queue:
            current = queue.popleft()
            if is_valid(current):
                result.append(current)
                found = True
            if found:
                continue  # Only collect valid strings with minimum removals
            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                next_str = current[:i] + current[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result if result else [""]
