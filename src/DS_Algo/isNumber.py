# Given a string s, return whether s is a valid number.

# For example, all the following are valid numbers:
#  "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", 
#  "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",
#   while the following are not valid numbers:
#      "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# Formally, a valid number is defined using one of the following definitions:
# 1. An integer number followed by an optional exponent.
# 2. A decimal number followed by an optional exponent.

# An integer number is defined with an optional sign '-' or '+' followed by digits.
# A decimal number is defined with an optional sign '-' or '+' followed by 
# one of the following definitions:
# 1. Digits followed by a dot '.'.
# 2. Digits followed by a dot '.' followed by digits.
# 3. A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' 
# followed by an integer number.
# The digits are defined as one or more digits.

# Constraints:
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase),
#  digits (0-9), plus '+', minus '-', or dot '.'.

# Example: 
# Input: s = "0"
# Output: true

# Input: s = "e"
# Output: false

# Input: s = "."
# Output: false

# Explanation
# 1. isInteger(s):
#     Checks if the string is a valid integer.
#     Allows optional + or - sign.
#     Must contain only digits after the sign.
# 2. isDecimal(s):
#     Checks if the string is a valid decimal.
#     Allows optional + or - sign.
#     Must contain a dot ..
#     At least one side of the dot must have digits.
# 3. Main Logic:
#     If the string contains 'e' or 'E', split it into base and exponent.
#     Base must be a valid integer or decimal.
#     Exponent must be a valid integer.
#     If no 'e' or 'E', check if it's a valid integer or decimal.

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), constant space used.

class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(s):
            # Check if s is a valid integer: optional sign followed by digits
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            # Check if s is a valid decimal number
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]

            if '.' not in s:
                return False

            integer_part, dot, fractional_part = s.partition('.')
            # Valid if at least one side of the dot has digits
            if not integer_part and not fractional_part:
                return False
            if integer_part and not integer_part.isdigit():
                return False
            if fractional_part and not fractional_part.isdigit():
                return False
            return True

        # Step 1: Split by 'e' or 'E' to separate base and exponent
        if 'e' in s or 'E' in s:
            base, _, exponent = s.lower().partition('e')
            return (isInteger(base) or isDecimal(base)) and isInteger(exponent)
        else:
            return isInteger(s) or isDecimal(s)


sol = Solution()
print(sol.isNumber("2"))           # True
print(sol.isNumber("0089"))        # True
print(sol.isNumber("-0.1"))        # True
print(sol.isNumber("abc"))         # False
print(sol.isNumber("1e"))          # False
print(sol.isNumber("53.5e93"))     # True
print(sol.isNumber("99e2.5"))      # False
