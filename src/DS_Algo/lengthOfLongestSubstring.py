# Given a string s, find the length of the longest substring without duplicate characters.
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # keeps track of the last seen index of each character.
        left = 0 # left is the start of the current window.
        max_length = 0 

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
