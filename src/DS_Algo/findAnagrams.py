# Given two strings s and p, return an array of all the start indices
#  of p's anagrams in s. You may return the answer in any order.

# Constraints:
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.

# Example:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# s = "cbaebabacd"
# p = "abc"
# # Output: [0, 6]
# # Explanation: "cba" at index 0 and "bac" at index 6 are anagrams of "abc"


# Step-by-Step Explanation
# 1. Initialize frequency arrays for 26 lowercase letters.
# 2. Build frequency map for string p.
# 3. Use a sliding window of size m (length of p) to scan through s.
# 4. For each character in s:
#     Add it to the window frequency.
#     If the window exceeds size m, remove the leftmost character.
#     If the window size is exactly m and the frequency matches p, record the start index.
# 5. Return all matching start indices.

# Let: n=len(s), mad=len(p)
# Time Complexity: O(n) — each character is processed once in the sliding window.
# Space Complexity: O(1) — fixed-size arrays of 26 elements (constant space).

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []  # No anagrams possible if p is longer than s

        # Frequency arrays for 'a' to 'z'
        target_freq = [0] * 26  # Frequency of characters in p
        window_freq = [0] * 26  # Frequency of current window in s

        # Build frequency map for p
        for char in p:
            target_freq[ord(char) - ord('a')] += 1

        result = []
        left = 0  # Start of the sliding window

        for right in range(n):
            # Add current character to the window
            window_freq[ord(s[right]) - ord('a')] += 1

            # Shrink window if its size exceeds m
            if right - left + 1 > m:
                window_freq[ord(s[left]) - ord('a')] -= 1
                left += 1

            # If window size equals m and frequencies match, record the index
            if right - left + 1 == m and window_freq == target_freq:
                result.append(left)

        return result

