# Given two binary strings a and b, return their sum as a binary string.

# Constraints:

# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# Time Complexity: O(max(n,m)), Where n and m are lengths of a and b
# Space Complexity: O(max(n,m)) For storing result

# Logic
# Let’s walk through the example:
#     Input: a = "1010", b = "1011"
# Step 1: Initialize pointers and carry
#     i = len(a) - 1 = 3
#     j = len(b) - 1 = 3
#     carry = 0
# Step 2: Loop through both strings from right to left
#     At each step:
#         Get current bits: bit_a, bit_b
#         Add them with carry
#         Compute new bit: total % 2
#         Update carry: total // 2
#         Append result
# Step 3: Reverse and join result
#     Final result list: ['1', '0', '1', '0', '1']
#     Reverse → "10101"
#     Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry
            carry = total // 2
            result.append(str(total % 2))

            i -= 1
            j -= 1

        return ''.join(reversed(result))

# Create an instance of the class
sol = Solution()

# Call the method with an input list
a, b = "1010", "1011"
output = sol.addBinary(a, b)

# Print the result
print(output)