# Given a string s, return the longest palindromic substring in s.

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Example:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"

# Method 1: Around Center**:
# Every palindrome is centered at a character (odd-length) or between two characters (even-length).
# For each index i, check both types.
# 2. Track the longest palindrome:
#     If the length of the current palindrome is greater than the previous longest, update start and end.
# 3. Return the substring:
#     Slice the string from start to end + 1.

# Time Complexity: O(n^2) — each center expansion can take up to O(n).
# Space Complexity: O(1) — no extra space used beyond variables.

# Example Walkthrough
# Input: "babad"

# Expand around index 0 → "b"
# Expand around index 1 → "aba"
# Expand around index 2 → "bab"
# Longest found: "bab" or "aba"
# Input: "cbbd"

# Expand around index 1 → "bb"
# Longest found: "bb"

# Method 2: using dynamic programming
# Step-by-Step Explanation
# 1. Initialize a 2D DP table dp[i][j]:
#     True if substring s[i:j+1] is a palindrome.
#     False otherwise.
# 2. Base cases:
#     All substrings of length 1 are palindromes.
#     Check substrings of length 2: if s[i] == s[i+1], mark as palindrome.
# 3. General case:
#     For substrings of length ≥ 3:
#         s[i] == s[j] and dp[i+1][j-1] == True → dp[i][j] = True
# 4. Track the longest palindrome:
#     Update start and max_len whenever a longer palindrome is found.

# Time Complexity: O(n^2) — nested loops for all substrings.
# Space Complexity: O(n^2) — DP table.

# Method 3: Manacher’s Algorithm Overview
# How Manacher’s Algorithm Works (Step-by-Step)
# 1. Preprocess the string:
#     Insert # between characters and at both ends to handle even-length palindromes uniformly.
#     Example: "abba" → "#a#b#b#a#"
# 2. Use a center-expansion strategy:
#     Maintain a center and right boundary of the current longest palindrome.
#     For each position i, find its mirror position relative to the center.
#     Use previously computed palindrome lengths to minimize expansion.
# 3. Expand around center i:
#     Try to expand the palindrome centered at i as far as possible.
#     Update center and right if the palindrome at i extends beyond right.
# 4. Track the longest palindrome:
#     After processing, find the maximum radius and its center.
#     Convert the center index back to the original string index.

# Manacher’s Algorithm finds the longest palindromic substring 
#     in linear time  O(n) by:
# 1. Preprocessing the string to handle even-length palindromes:
#     Insert # between characters and at both ends.
#     Example: "babad" → "#b#a#b#a#d#"
# 2. Using a center-expansion strategy:
#     For each character in the preprocessed string, expand outward to find the longest palindrome centered there.
#     Use previously computed palindrome lengths to avoid redundant checks.
# 3. Tracking the longest palindrome:
#     Keep track of the center and radius of the longest palindrome found so far.

# Time Complexity: O(n) — linear scan with efficient reuse of previous computations.
# Space Complexity: O(n) — for the radii array and preprocessed string.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expand_from_center(s, i, i)       # Odd-length palindrome
            len2 = self.expand_from_center(s, i, i + 1)   # Even-length palindrome
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand_from_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    # Method 2: Dynamic Programming
    def longestPalindromeDP(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] will be True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check substrings of length > 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        return s[start:start + max_len]

    # Method 3: Manacher's Algorithm
    def longestPalindromeManacher(self, s: str) -> str:
        if not s or s == s[::-1]:
            return s

        # Step 1: Preprocess the string
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        radii = [0] * n

        center = radius = 0

        # Step 2: Expand around each center
        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                radii[i] = min(radius - i, radii[mirror])

            # Try to expand palindrome centered at i
            a, b = i + (1 + radii[i]), i - (1 + radii[i])
            while a < n and b >= 0 and t[a] == t[b]:
                radii[i] += 1
                a += 1
                b -= 1

            # Update center and radius if expanded beyond current boundary
            if i + radii[i] > radius:
                center = i
                radius = i + radii[i]

        # Step 3: Find the longest palindrome
        max_len = max(radii)
        max_center = radii.index(max_len)

        # Convert back to original string indices
        start_index = (max_center - max_len) // 2
        return s[start_index:start_index + max_len]
        