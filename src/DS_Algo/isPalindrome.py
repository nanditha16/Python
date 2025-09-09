# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Method i : using Slicing ([::-1]) - For quick, readable code in small-scale use → Slicing is fine.
# Time Complexity:
    # Reversing the string: O(n)
    # Comparing strings: O(n)
    # Total: O(n)
# Space Complexity: Creates a new reversed string →  O(n) extra space 

# Method 2: using pointers - For performance and memory efficiency, especially with large strings 
# Time Complexity: Single pass through the string → O(n) 
# Space Complexity: No extra space used → O(1)

# Two pointers:
# 1. left starts at the beginning, right at the end.
# 2. Compare characters: If s[left] != s[right], it's not a palindrome.
# 3. Move inward: Increment left, decrement right.
# 4. Stop when pointers meet or cross.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered string is equal to its reverse
        return filtered == filtered[::-1]

    # Method 2
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# Create an instance of the class
sol = Solution()

# Call the method with an input list

output1 = sol.isPalindrome("A man, a plan, a canal: Panama")
output2 = sol.is_palindrome("cat")

# Print the result
print(output1)
print(output2)
