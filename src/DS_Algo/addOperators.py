# Given a string num that contains only digits and an integer target, 
# return all possibilities to insert the binary operators '+', '-', 
# and/or '*' between the digits of num so that the resultant expression 
# evaluates to the target value.

# Note that operands in the returned expressions should not contain leading
#  zeros.

# Note that a number can contain multiple digits.

# Constraints:
# 1 <= num.length <= 10
# num consists of only digits.
# -2^31 <= target <= 2^31 - 1

# Example:
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

# Input: num = "3456237490", target = 9191
# Output: []
# Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

# Step-by-Step Explanation
# 1. Backtracking is used to explore all possible combinations of operators between digits.
# 2. At each step, we:
#     Choose a substring of digits (operand).
#     Skip if it starts with '0' and is longer than one digit.
#     Try adding each operator (+, -, *) before the operand.
# 3. Multiplication is tricky due to precedence:
#     We keep track of the last operand (last) and adjust the total accordingly:
#         value - last + last * curr simulates correct multiplication precedence.
# 4. If we reach the end of the string and the expression evaluates to target, we add it to the result.

# Edge Case Handling
#     Leading zeros are skipped ("05" is invalid, "0" is valid).
#     Handles negative targets and large numbers.
#     Works for strings of length up to 10.

# Time Complexity: Worst case: O(4^n) 
#     Each digit can be followed by 3 operators or be part of a longer number.
#     Exponential due to recursive branching.
# Space Complexity: O(n) for recursion stack and path string.

from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(index, path, value, last):
            """
            index: current position in num
            path: current expression string
            value: current evaluated result
            last: last operand used (for multiplication handling)
            """
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i != index and num[index] == '0':
                    break

                curr_str = num[index:i+1]
                curr = int(curr_str)

                if index == 0:
                    # First number, no operator needed
                    backtrack(i+1, curr_str, curr, curr)
                else:
                    # Addition
                    backtrack(i+1, path + '+' + curr_str, value + curr, curr)
                    # Subtraction
                    backtrack(i+1, path + '-' + curr_str, value - curr, -curr)
                    # Multiplication
                    backtrack(i+1, path + '*' + curr_str, value - last + last * curr, last * curr)

        backtrack(0, "", 0, 0)
        return res
