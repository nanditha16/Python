# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
# If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. 
# Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        sign = 1
        if i < n and s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Step 4: Check for overflow
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num
