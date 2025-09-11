# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.

# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Time	O(4ⁿ)	Each digit can map to up to 4 letters (e.g., '7', '9')
# Space	O(n)	Recursion depth and path string

# Example:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Input: digits = ""
# Output: []

# Input: digits = "2"
# Output: ["a","b","c"]

# Step-by-Step Explanation
# Check for empty input:
#     If digits is empty, return an empty list.
# Define digit-to-letter mapping:
#     Use a dictionary phone_map to map digits to corresponding letters.
# Use backtracking:
#     Start from index 0 and build combinations recursively.
#     At each step, append one letter from the current digit’s mapping.
#     When the path length equals the input length, add it to the result.
# Return result:
#     After recursion completes, return the list of combinations.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            for char in phone_map[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return result
