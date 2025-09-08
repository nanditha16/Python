# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Time Complexity:    
#     Sorting each word: O(klogk)
#     For n words:  O(n⋅klogk) Where n is number of words, k is average word length
# Space Complexity: O(n⋅k) for storing grouped anagrams


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Initialize a dictionary - use a defaultdict(list) to group words by their sorted character key
        anagram_map = defaultdict(list)

        # Step 2: Iterate through each word
            # For each word:
            #     Sort its characters → this becomes the key
            #     Append the word to the list for that key
        for word in strs:
            # Sort the word to get the key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        # Step 3: Return grouped values
        return list(anagram_map.values())

# Create an instance of the class
sol = Solution()

# Call the method with an input list
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = sol.groupAnagrams(input)

# Print the result
print(output)
