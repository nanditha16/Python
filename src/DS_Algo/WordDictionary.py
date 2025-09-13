# Design a data structure that supports adding new words and finding if 
# a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure 
# that matches word or false otherwise. word may contain dots '.' where dots
#  can be matched with any letter.
 
# Constraints:
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.

#  Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


# WordDictionary class using a Trie (prefix tree) to support:
#     Efficient word addition
#     Flexible search with . wildcard, which can match any character

# Step-by-Step Explanation
# 1. TrieNode Class
#     Each node stores:
#     children: a dictionary mapping characters to child nodes.
#     is_end: a boolean flag indicating if a word ends at this node.
# 2. addWord(word)
#     Traverse the Trie character by character.
#     Create new nodes as needed.
#     Mark the final node as the end of a word.
# 3. search(word)
#     Uses a helper _search_recursive to support recursion.
#     If a character is ., it tries all children at that level.
#     If a character is a letter, it follows the corresponding child node.
#     Returns True if a valid word is matched.

# addWord(word)
#     Time: O(n), where n is the length of the word
#     Space: O(n) for new nodes
# search(word)
# Time: Worst-case: O(n × 26^d), where:
#     n = length of the word
#     d = number of . wildcards
#     In practice: much faster due to early pruning
# Space: O(h) for recursion stack (h = length of word)

# Why This Is Optimized
#     Efficient wildcard handling via recursion
#     Minimal memory usage due to shared prefixes
#     Scales well with large dictionaries
#     Fast lookup for both exact and fuzzy matches

# Problem Recap: 
#     You can add words like "bad", "dad", "mad" to the dictionary.
#     You can search for exact matches like "bad" or fuzzy matches like:
#     "b.." → matches "bad"
#     ".ad" → matches "bad", "dad", "mad"
# How Recursion Handles Wildcards
#     Key Idea: When you encounter a . in the search word, it can match any character. So instead of following a specific path in the Trie, you must try all possible children at that level.

# Step-by-Step Example
#     Let’s say you added "bad" and "dad" to the Trie, and now you search for ".ad".

# Trie Structure:
# root
#  ├── b
#  │    └── a
#  │         └── d (end)
#  └── d
#       └── a
#            └── d (end)
# Search: ".ad"
# Index 0: . → Try all children of root: 'b' and 'd'
# Index 1: 'a' → Follow 'a' from 'b' and 'd'
# Index 2: 'd' → Follow 'd' from 'a'
# End of word: Check if current node is end of a word → 
# So ".ad" matches both "bad" and "dad".

# Code Logic for Wildcard
# if char == '.':
#     for child in node.children.values():
#         if self._search_recursive(word, index + 1, child):
#             return True
#     return False

# Try all children at current node.
# Recursively search the rest of the word from each child.
# Return True if any path leads to a valid word.
# Time Complexity Worst-case: O(n⋅26^d)
#     where:
#     n = length of the word
#     d = number of . wildcards
# Best-case: O(n) — when there are no wildcards and the word exists.

# Space Complexity: O(h) — height of the Trie for recursion stack

class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.is_end = False  # Marks end of a valid word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Root of the Trie

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            # Create a new node if character not present
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of the word
        node.is_end = True

    def search(self, word: str) -> bool:
        # Start recursive search from root
        return self._search_recursive(word, 0, self.root)

    def _search_recursive(self, word: str, index: int, node: TrieNode) -> bool:
        # Base case: reached end of word
        if index == len(word):
            return node.is_end

        char = word[index]

        if char == '.':
            # Try all possible children for wildcard
            for child in node.children.values():
                if self._search_recursive(word, index + 1, child):
                    return True
            return False
        else:
            # Regular character: follow the path
            if char not in node.children:
                return False
            return self._search_recursive(word, index + 1, node.children[char])

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)