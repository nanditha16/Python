# You have intercepted a secret message encoded as a string of numbers. 
# The message is decoded via the following mapping:
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'

# However, while decoding the message, you realize that there are many 
# different ways you can decode the message because some codes are contained
#  in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a 
# valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number 
# of ways to decode it. If the entire string cannot be decoded 
# in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# Example:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero 
# ("6" is different from "06"). In this case, the string is not a valid encoding, 
# so return 0.


# Method 1: Dynamic Programming
# Step-by-Step Explanation
# 1. Create a DP array dp where dp[i] represents the number of ways to decode the substring s[0:i].
# 2. Initialize dp[0] = 1 (an empty string has one way to be decoded) and dp[1] = 1 if s[0] != '0' else 0.
# 3. Iterate through the string from index 2 to len(s):
#     - If s[i-1] (the current character) is not '0', then dp[i] += dp[i-1] (the current character can stand alone).
#     - If the two-character substring s[i-2:i] forms a valid number between 10 and 26, then dp[i] += dp[i-2] (the two characters can be decoded together).
# 4. The final answer will be in dp[len(s)].   

# Step-by-Step Explanation
# 1. Initialization:
#     dp[i] represents the number of ways to decode the substring s[:i].
#     dp[0] = 1: empty string has one valid decoding.
#     dp[1] = 1: if s[0] != '0', there's one way to decode the first character.
# 2. Iterate from index 2 to n:
#     Single digit check: If s[i-1] is between '1' and '9', add dp[i-1].
#     Two digit check: If s[i-2:i] is between '10' and '26', add dp[i-2].
# 3. Return dp[n]: total number of decoding ways.

# Time Complexity: O(n) — one pass through the string.
# Space Complexity: O(n) — for the dp array.
# Can be optimized to  O(1) using two variables instead of an array.

# Method 2: recursive dynamic programming solution with memoization using a dictionary (dp) to store intermediate results.

# Step-by-Step Explanation
# 1. Base Case:
#     dp[len(s)] = 1: An empty string has one valid decoding.
# 2. Iterate Backwards:
#     From the end of the string to the beginning.
# 3. Handle '0':
#     If s[i] == '0', it can't be decoded → dp[i] = 0.
# 4. Single Digit Decode:
#     If s[i] != '0', then dp[i] = dp[i+1].
# 5. Two Digit Decode:
#     If s[i:i+2] is between "10" and "26", then add dp[i+2].
# 6. Return dp[0]:
#     This gives the total number of ways to decode the full string.

# Edge Case Handling
#     "0" → returns 0
#     "06" → returns 0
#     "10" → returns 1
#     "101" → returns 1
#     "100" → returns 0

# Time Complexity: O(n) — each index is processed once.
# Space Complexity: O(n) — dictionary dp stores results for each index.

class Solution:
    def numDecodingsDP(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has one way to decode
        dp[1] = 1  # First character is guaranteed not '0' here

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2:i])

            # Check if single digit is valid (1-9)
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            # Check if two digits form a valid code (10-26)
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

        # Method 2: recursive dynamic programming solution with memoization using a dictionary (dp) to store intermediate results.
    def numDecodingsRecursiveDP(self, s: str) -> int:
        dp = {len(s): 1}  # Base case: empty string has one valid decoding

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0  # No valid decoding starts with '0'
            else:
                dp[i] = dp[i + 1]  # Single digit decoding

                # Check if two-digit decoding is valid
                if (i + 1 < len(s)) and (
                    (s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456")
                ):
                    dp[i] += dp[i + 2]

        return dp[0]
