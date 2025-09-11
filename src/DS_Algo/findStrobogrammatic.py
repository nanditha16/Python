# Time	O(5^(n/2))	Each level adds up to 5 pairs
# Space	O(5^(n/2))	Result list and recursion stack

# Step-by-Step Explanation
# Strobogrammatic Pairs:
#     Valid digit pairs that look the same when rotated:
#     ('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')
# Recursive Construction:
#     Build from inside out:
#     Base case n == 0: return [""]
#     Base case n == 1: return ["0", "1", "8"]
# Avoid Leading Zeros:
#     When building the outermost layer (n == total_len), skip '0' as the first digit.
# Combine Pairs Around Middle:
#     For each middle string, wrap it with each valid pair to form a larger strobogrammatic number.

from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

        def build(n: int, total_len: int) -> List[str]:
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            middles = build(n - 2, total_len)
            result = []

            for middle in middles:
                for a, b in pairs:
                    # Avoid leading zeros
                    if n == total_len and a == '0':
                        continue
                    result.append(a + middle + b)
            return result

        return build(n, n)
