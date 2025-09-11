
# In an alien language, surprisingly, they also use English lowercase letters, 
# but possibly in a different order. The order of the alphabet is some 
# permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order 
# of the alphabet, return true if and only if the given words are sorted 
# lexicographically in this alien language.


# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

# Example:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], 
# hence the sequence is unsorted.

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string 
# is shorter (in size.) According to lexicographical rules "apple" > "app", 
# because 'l' > '∅', where '∅' is defined as the blank character which is less 
# than any other character (More info).

# Time complexity: O(N⋅L)
# Where:
# N is the number of words.
# L is the average length of the words.
# We compare each pair of words character by character.
# Space complexity: O(1)
# The character-to-index mapping uses a fixed size of 26 characters, so it’s constant space.

#  Intuition
# The problem is about verifying if a list of words is sorted according to
#  a custom alphabet order used in an alien language. Since the alien language 
#  uses the same lowercase English letters but in a different order, 
#  we need to compare words based on this new character ranking rather 
#  than the standard English order.

# Approach
# 1. Create a mapping from each character to its index in the alien alphabet. This allows constant-time lookup for character precedence.
# 2. Iterate through each pair of adjacent words in the list.
# 3. For each pair:
#     Compare characters one by one using the alien order.
#     If characters differ, use the mapping to determine which word should come first.
#     If all characters match up to the length of the shorter word, 
#     ensure the shorter word comes first (e.g., "app" should come before "apple").
# 4. If any pair is out of order, return False. Otherwise, return True.

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Step 1: Create a mapping from each character to its index in the alien alphabet
        order_index = {char: idx for idx, char in enumerate(order)}

        # Step 2: Compare each pair of adjacent words
        for i in range(len(words) - 1):
            if not self.in_correct_order(words[i], words[i + 1], order_index):
                return False
        return True

    def in_correct_order(self, word1: str, word2: str, order_index: dict) -> bool:
        # Step 3: Compare characters of both words
        for c1, c2 in zip(word1, word2):
            if order_index[c1] < order_index[c2]:
                return True
            elif order_index[c1] > order_index[c2]:
                return False
        # Step 4: If all characters are equal so far, shorter word should come first
        return len(word1) <= len(word2)


sol = Solution()
print(sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))  # True
print(sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))  # False
print(sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))  # False

