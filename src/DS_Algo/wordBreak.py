# Given a string s and a dictionary of strings wordDict, 
# return true if s can be segmented into a space-separated sequence 
# of one or more dictionary words.

# Note that the same word in the dictionary may be reused 
# multiple times in the segmentation.

# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

# Example:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as 
# "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Method 1: Dynamic Programming (Forward)
# Step-by-Step Explanation
# 1. Initialize:
#     dp[i] means whether s[:i] can be segmented using words from wordDict.
#     dp[0] = True because an empty string is trivially segmentable.
# 2. Iterate over i from 1 to n:
#     For each i, check all substrings s[j:i] where j < i.
#     If dp[j] is True and s[j:i] is in the dictionary, then dp[i] = True.
# 3. Return dp[n]:
#     This tells whether the entire string s can be segmented.

# Edge Case Handling
#     Empty string → returns True
#     Dictionary with overlapping words → handled correctly
#     Repeated use of the same word → allowed
#     No valid segmentation → returns False

# Time Complexity: O(n^2) — nested loop over i and j, and substring checks.
# Space Complexity: O(n+m) — dp array of size n+1, and word_set of size m.

# Method 2: Dynamic Programming (Backward)
# Step-by-Step Explanation
# 1. Initialize:
#     dp[i] means whether s[i:] can be segmented using words from wordDict.
#     dp[n] = True because an empty string is trivially segmentable.
# 2. Iterate over i from n-1 down to 0:
#     For each i, check all substrings s[i:j] where j > i.
#     If dp[j] is True and s[i:j] is in the dictionary, then dp[i] = True.
# 3. Return dp[0]:
#     This tells whether the entire string s can be segmented.  

# How Is This Better?
# 1. Avoids Substring Creation in Inner Loop
#     Instead of checking all s[j:i] substrings like in the classic DP approach,
#      this version checks only substrings that match dictionary words.
#     This can be faster in practice, especially when wordDict contains short
#      words and s is long.
# 2. Early Break Optimization
#     As soon as dp[i] becomes True, it breaks out of the inner loop.
#     This avoids unnecessary checks once a valid segmentation is found.
# 3. Bottom-Up from End
#     Starts from the end of the string and works backward.
#     This can be more intuitive when thinking in terms of "can I build a valid 
#      sentence from this point forward?"

# Edge Case Handling
#     Empty string → returns True
#     Dictionary with overlapping words → handled correctly
#     Repeated use of the same word → allowed
#     No valid segmentation → returns False

# Time Complexity: Worst-case:  O(n⋅m⋅k)
#     Where:
#     n = length of s
#     m = number of words in wordDict
#     k = average length of words
# Space Complexity: O(n) — for the dp array

# Methos 3:  Trie-based optimization 
# Step-by-Step Explanation
# 1. Build a Trie:
#     Each word in wordDict is inserted character by character.
#     is_word marks the end of a valid word.
# 2. DFS with Memoization:
#     Start from index 0 and try to match prefixes using the Trie.
#     If a valid word is found (node.is_word), recursively check the rest of the string.
#     Use memo to cache results and avoid recomputation.

# Why Trie Is Better
#     1. Efficient Prefix Matching: Instead of checking every substring,
#  we only follow valid paths in the Trie.
#     2. Reduces Redundant Checks: Especially helpful when wordDict 
# has many overlapping prefixes.
#     3. Scales Better: For large dictionaries and long strings,
#  this can outperform brute-force DP.

# Time Complexity: Worst-case: O(n^2 ) But often faster due to early pruning via Trie.
# Space Complexity: O(n+m⋅k)
#     n for memoization
#     m = number of words
#     k = average word length (Trie size)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

from typing import List
class Solution:
    def wordBreakForward(self, s: str, wordDict: List[str]) -> bool:      
        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        n = len(s)
        
        # dp[i] will be True if s[0:i] can be segmented into words in the wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can be segmented
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # No need to check further if we found a valid segmentation i.e if s[0:i] is segmentable
        
        return dp[n]
    
    # Method 2: Dynamic Programming (Backward)
    def wordBreakBackward(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string is segmentable

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

    # Method 3: Trie-based optimization    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Build Trie from wordDict
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        memo = {}

        def dfs(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]

            node = root
            for i in range(index, len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.is_word and dfs(i + 1):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return dfs(0)
