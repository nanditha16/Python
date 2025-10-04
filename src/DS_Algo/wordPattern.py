# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Constraints:
#     1 <= pattern.length <= 300
#     pattern contains only lower-case English letters.
#     1 <= s.length <= 3000
#     s contains only lowercase English letters and spaces ' '.
#     s does not contain any leading or trailing spaces.
#     All the words in s are separated by a single space.

# Example :
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Time Complexity:
# Splitting the string: O(n) where nnn is the length of s.
# Iterating through pattern and words: O(m) where mmm is the length of pattern.
# Dictionary operations are O(1) on average.
# Total: O(n+m)

# Space Complexity:
# Two dictionaries storing up to mmm entries each.
# Total: O(m)

# Step-by-Step Explanation
# 1. Split the string s into words using split().
# 2. Check length: If the number of words doesn't match the length of the pattern, return False.
# 3. Create two dictionaries:
#     char_to_word: maps each character in pattern to a word in s.
#     word_to_char: maps each word in s to a character in pattern.
# 4. Iterate through the pattern and words simultaneously:
#     If the character is already mapped, check if it maps to the current word. If not, return False.
#     If the character is not mapped, check if the word is already mapped to another character. If yes, return False.
#     Otherwise, create the mapping in both dictionaries.
# 5. If all checks pass, return True.

# Edge Case Handling
#     Length mismatch: If the number of characters in pattern ≠ number of words in s, return False.
#     Multiple characters mapping to same word: Prevents many-to-one mapping.
#     Multiple words mapping to same character: Prevents one-to-many mapping.
#     Empty strings: Not needed here as per constraints (no leading/trailing spaces, all lowercase letters).


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Step 1: Split the input string `s` into a list of words
        words = s.split()

        # Step 2: Check if the number of pattern characters matches the number of words
        # If not, it's impossible to have a one-to-one mapping
        if len(pattern) != len(words):
            return False

        # Step 3: Create two dictionaries to store the bijection mappings
        char_to_word = {}  # Maps pattern character to word
        word_to_char = {}  # Maps word to pattern character

        # Step 4: Iterate through each character and corresponding word
        for char, word in zip(pattern, words):
            # Case 1: Character already has a mapping
            if char in char_to_word:
                # Check if the mapped word matches the current word
                if char_to_word[char] != word:
                    return False  # Mismatch found
            else:
                # Case 2: Word is already mapped to a different character
                if word in word_to_char:
                    return False  # This word is already mapped to another character
                # Create new mappings in both dictionaries
                char_to_word[char] = word
                word_to_char[word] = char

        # Step 5: All checks passed, return True
        return True


sol = Solution()

print(sol.wordPattern("abba", "dog cat cat dog"))   # True
print(sol.wordPattern("abba", "dog cat cat fish"))  # False
print(sol.wordPattern("aaaa", "dog cat cat dog"))   # False
print(sol.wordPattern("abc", "dog dog dog"))        # False
print(sol.wordPattern("abc", "dog cat dog"))        # False
print(sol.wordPattern("abc", "dog cat mouse"))      # True
