# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= xn <= 10^4

# Time Complexity: O(logn) — binary exponentiation.
# Space Complexity: O(1) — constant space.

# Example:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Step-by-Step Explanation
# 1. Negative exponent:
#     If n < 0, invert x and make n positive.
#     Example: x = 2, n = -2 → x = 1/2, n = 2.
# 2. Binary exponentiation:
#     Multiply result by x only when the current bit of n is 1.
#     Square x each time and halve n.
# 3. Loop until n == 0:
#     This ensures logarithmic time complexity.

# Edge Case Handling
#     x = 0, n > 0: returns 0.0
#     x = 1, any n: returns 1.0
#     x = -1, even/odd n: returns 1.0 or -1.0
#     n = 0: returns 1.0 (any number to the power 0 is 1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result
