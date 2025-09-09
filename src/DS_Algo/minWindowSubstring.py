# Given two strings s and t of lengths m and n respectively, return 
# the minimum window substring of s such that every character in t (including duplicates) 
# is included in the window. If there is no such substring, return the empty string.

# The testcases will be generated such that the answer is unique.

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

# Time Complexity: O(m+n) Each character is visited at most twice (once by right, once by left)
# Space Complexity: O(n) For storing character counts

# Step 1: Count characters in t
# Step 2: Use sliding window
#     Expand right pointer to include characters
#     Track counts in window_counts
#     When all required characters are matched (formed == required), try shrinking from left
# Step 3: Update minimum window
#     If current window is smaller than previous best, update min_window
# Step 4: Return result
#     Slice s using min_window indices
#     Output: "BANC"

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)

        # Sliding window pointers and counters
        left = 0
        formed = 0
        window_counts = {}
        min_len = float("inf")
        min_window = (0, 0)

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # Try to shrink the window from the left
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                # Remove leftmost character
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1

        if min_len == float("inf"):
            return ""
        return s[min_window[0]:min_window[1] + 1]
    
# Create an instance of the class
sol = Solution()

# Call the method with an input list
s, t = "ADOBECODEBANC", "ABC"
output = sol.minWindow(s, t)

# Print the result
print(output)
