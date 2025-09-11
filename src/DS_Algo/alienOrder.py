# There is a new alien language that uses the English alphabet. 
# However, the order of the letters is unknown to you.
# You are given a list of strings words from the alien language's dictionary. 
# Now it is claimed that the strings in words are sorted lexicographically 
#     by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words 
# cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien 
# language sorted in lexicographically increasing order by the new 
# language's rules. If there are multiple solutions, return any of them.

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

# Input: words = ["z","x"]
# Output: "zx"

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

# Time Complexity: O(N × L)
#     N = number of words
#     L = average length of words
#     Building graph: comparing adjacent words → O(N × L)
#     Topological sort: O(V + E), where V = unique characters, E = edges
# Space Complexity: O(V + E)
#     V = number of unique characters
#     E = number of edges (dependencies)

# Step-by-Step Explanation
# Initialize Graph:
#     Create a directed graph where each node is a character.
#     Initialize in-degree for each character to 0.
# Build Graph:
#     Compare each pair of adjacent words.
#     Find the first differing character and create a directed edge from w1[j] to w2[j].
#     If w1 is longer and is a prefix of w2, it's invalid → return "".
# Topological Sort:
#     Use Kahn’s algorithm (BFS) to sort characters.
#     Start with characters that have in-degree 0.
#     Append to result and reduce in-degree of neighbors.
# Cycle Detection:
#     If result length is less than total unique characters → cycle exists → return "".

from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Create graph and in-degree map
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""  # Invalid order: prefix case
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # Step 3: Topological sort using Kahn's algorithm
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check for cycle
        if len(result) != len(in_degree):
            return ""

        return "".join(result)
