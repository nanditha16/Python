# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.

# Constraints:
# 0 <= s.length, t.length <= 10^4
# s and t consist of lowercase letters, uppercase letters, and digits.

# Time Complexity: O(n) — where n is the length of the shorter string.
# Space Complexity: O(1) — no extra space used.

# Explanation
#     We first ensure s is the shorter string to simplify logic.
#     If the length difference is more than 1, return False.
#     We iterate through both strings:
#         If we find a mismatch:
#             If lengths are equal → check if the rest of the strings match after replacing one character.
#             If lengths differ → check if the rest of s matches t after skipping one character in t.
#     If no mismatch is found, the only valid case is when t has one extra character at the end.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)

        # Ensure s is the shorter string
        if len_s > len_t:
            return self.isOneEditDistance(t, s)

        # Length difference greater than 1 means more than one edit
        if len_t - len_s > 1:
            return False

        for i in range(len_s):
            if s[i] != t[i]:
                # If lengths are equal, check for replacement
                if len_s == len_t:
                    return s[i+1:] == t[i+1:]
                else:
                    # If lengths differ, check for insertion in s or deletion in t
                    return s[i:] == t[i+1:]

        # If all previous characters matched, check if t has one extra character
        return len_s + 1 == len_t

sol = Solution()

print(sol.isOneEditDistance("ab", "acb"))  # True (insert 'c')
print(sol.isOneEditDistance("", ""))       # False (no edits)
print(sol.isOneEditDistance("abc", "ab"))  # True (delete 'c')
print(sol.isOneEditDistance("abc", "adc")) # True (replace 'b' with 'd')
print(sol.isOneEditDistance("abc", "abc")) # False (no edits)
