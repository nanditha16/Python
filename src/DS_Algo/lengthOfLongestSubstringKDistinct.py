# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# Constraints:
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50

# Time Complexity: O(n) — each character is visited at most twice.
# Space Complexity: O(k) — for the character count dictionary.

# Explanation
# To solve Longest Substring with At Most K Distinct Characters, we can use the sliding 
# window technique with a hash map (dictionary) to track character frequencies.

# Use two pointers left and right to define a sliding window.
# Expand the window by moving right and adding characters to char_count.
# If the number of distinct characters exceeds k, shrink the window from the left.
# Track the maximum window size that satisfies the condition.

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0

        left = 0
        max_len = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            char_count[s[right]] += 1

            # Shrink window if more than k distinct characters
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


sol = Solution()

print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))  # Output: 3 ("ece")
print(sol.lengthOfLongestSubstringKDistinct("aa", 1))     # Output: 2 ("aa")
print(sol.lengthOfLongestSubstringKDistinct("abcadcacacaca", 3))  # Output: 11
