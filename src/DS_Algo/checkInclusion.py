# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Constraints:
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.

# Example:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Step-by-Step Explanation
# 1. Edge Case: If s1 is longer than s2, return False.
# 2. Frequency Arrays:
#     Use two arrays of size 26 (for lowercase letters).
#     s1_freq: frequency of characters in s1.
#     window_freq: frequency of current window in s2.
# 3. Initialize First Window:
#     Fill both arrays for the first len(s1) characters.
# 4. Compare:
#     If the first window matches s1_freq, return True.
# 5. Slide the Window:
#     For each new character in s2, update window_freq.
#     Remove the character that slides out of the window.
#     Compare the updated window_freq with s1_freq.
# 6. Return:
#     If any window matches, return True.
#     If no match is found, return False.

# Let: n=len(s2), m=len(s1)
# Time Complexity: O(n) — each character is processed once in the sliding window.
# Space Complexity: O(1) — fixed-size arrays of 26 elements (constant space).

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False  # s1 can't be a permutation of any substring in s2

        # Frequency arrays for 26 lowercase letters
        s1_freq = [0] * 26
        window_freq = [0] * 26

        # Build frequency map for s1 and the first window in s2
        for i in range(len_s1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if s1_freq == window_freq:
            return True

        # Slide the window over s2
        for i in range(len_s1, len_s2):
            # Add new character to the window
            window_freq[ord(s2[i]) - ord('a')] += 1
            # Remove the character that is no longer in the window
            window_freq[ord(s2[i - len_s1]) - ord('a')] -= 1

            # Compare frequency maps
            if window_freq == s1_freq:
                return True

        return False
