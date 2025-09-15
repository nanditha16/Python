# Given two non-negative integers, num1 and num2 represented as string,
#  return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for
#  handling large integers (such as BigInteger).
#   You must also not convert the inputs to integers directly.

# Constraints:
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

# Example:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Input: num1 = "456", num2 = "77"
# Output: "533"

# Input: num1 = "0", num2 = "0"
# Output: "0"

# Manual Digit-by-Digit Addition - to add two non-negative integers represented as strings without
#  converting them to integers directly and without using any big integer libraries

# How It Works:
#     Start from the end of both strings (least significant digit).
#     Add digits one by one, keeping track of the carry.
#     Append the result to a list and reverse it at the end to get the correct order.

# Time Complexity: O(max(n, m))
#     Where n = len(num1) and m = len(num2).
#     We process each digit once from both strings, starting from the end.
#     The loop runs at most max(n, m) + 1 times (the +1 is for a possible final carry).
# Space Complexity: **O(max(n, m the result in a list of digits, which will be at most max(n, m) + 1 characters long.
#     No additional space is used beyond that (excluding input).

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            # Instead of int(num1[i]), we use: ord(num1[i]) - ord('0')
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        return ''.join(reversed(result))


sol = Solution()
print(sol.addStrings("11", "123"))     # Output: "134"
print(sol.addStrings("456", "77"))     # Output: "533"
print(sol.addStrings("0", "0"))        # Output: "0"
