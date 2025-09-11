# Given an input string s and a pattern p, implement regular expression matching 
# with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Constraints:
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*',
#  there will be a previous valid character to match.

# Example:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'.
#  Therefore, by repeating 'a' once, it becomes "aa".

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Method 1: Using Dynamic Programming
# Step-by-Step Explanation
# Initialize DP Table:
#     dp[i][j] means s[:i] matches p[:j].
#     dp[0][0] = True because empty string matches empty pattern.
# Pre-fill for patterns like "a*":
#     If p[j-1] == '*', check if dp[0][j-2] is True.
# Iterate through s and p:
#     If characters match or p[j-1] == '.', inherit from dp[i-1][j-1].
# If p[j-1] == '*', consider:
#     Zero occurrence: dp[i][j-2]
#     One or more: if p[j-2] == s[i-1] or p[j-2] == '.', then dp[i-1][j]
# Return dp[m][n]:
#     Final result: does full s match full p.

# Time	O(m × n)	Nested loops over s and p
# Space	O(m × n)	DP table of size (m+1) × (n+1)
# Where: m = len(s),  n = len(p)

# Method 2: Using Recursive Version with Memoization

# Step-by-Step Explanation
# Memoization with @lru_cache:
#     Caches results of recursive calls to avoid recomputation.
# Recursive Function dp(i, j):
#     Returns True if s[i:] matches p[j:].
# Base Case:
#     If j == len(p), pattern is exhausted → return whether i == len(s).
# Character Match Check:
#     first_match = s[i] == p[j] or p[j] == '.'.
# Handle *:
#     If p[j+1] == '*', two choices:
#     kip p[j]* → dp(i, j+2)
#     Use p[j]* if first_match → dp(i+1, j)
# No * Case:
#     Move both pointers if characters match → dp(i+1, j+1)

# Time	O(m × n)	Memoized calls for each (i, j) pair
# Space	O(m × n)	Cache and recursion stack
# Where: m = len(s), n = len(p)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Zero occurrence of the character before '*'
                    dp[i][j] = dp[i][j - 2]
                    # One or more occurrences if preceding char matches
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]


    def isMatchRecurssive(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            # Base case: if pattern is exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' in pattern
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two options:
                # 1. Skip the '*' and preceding char (zero occurrence)
                # 2. Use '*' if first_match is True (consume one char from s)
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Move both pointers if current characters match
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)
