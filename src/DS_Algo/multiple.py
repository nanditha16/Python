# Given two integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# Time: O(m⋅n)
# Space: O(m+n)

# Sign Handling:
# Track if the result should be negative using a boolean negative.
# Strip the - sign from inputs before processing.

# Core Multiplication:
# Same as before: multiply digit by digit and store in a result array.

# Final Result:
# Convert the result array to a string.
# Add - sign if negative is True.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:          
        # Handle sign
        negative = False
        if num1[0] == '-':
            negative = not negative
            num1 = num1[1:]
        if num2[0] == '-':
            negative = not negative
            num2 = num2[1:]

        # Edge case: if either number is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse both strings
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Multiply digits
        for i in range(m):
            for j in range(n):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                result[i + j] += digit1 * digit2
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert to string
        result_str = ''.join(str(d) for d in reversed(result))

        # Add negative sign if needed
        return '-' + result_str if negative else result_str

# Create an instance of the class
sol = Solution()

# Call the method with an input list
num1 = "123"
num2 = "456"
output = sol.multiply(num1,num2 )

# Print the result
print(output)
