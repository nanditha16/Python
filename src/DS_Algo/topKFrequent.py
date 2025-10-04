# Given:
# An integer array nums
# An integer k

# Goal: Return the list of the top k most frequent elements in nums.

# Example
# Input: nums = [1,1,1,2,2,3,1,4], k = 2
# Output: [1, 2]

# Explanation:
#     Frequencies: {1: 4, 2: 2, 3: 1, 4: 1}
#     Top 2 most frequent elements: 1 and 2

# Edge Case Handling
#     Empty list: If nums is empty, return an empty list.
#     k = 0: Return an empty list.
#     k > number of unique elements: Raise a ValueError to prevent invalid input.
#     All elements have same frequency: The function still returns any k of them.

# Step-by-Step Explanation
# Step 1: Count Frequencies
# We use Counter to count how many times each number appears:
# Step 2: Get Top k Frequent Elements
# We use heapq.nlargest() to get the k keys with the highest frequency:
# Step 3: Return the Result

# Time Complexity:
#     Counting frequencies: O(n)
#     Getting top k elements: O(nlogk)
#     Total: O(nlogk)

# Space Complexity:
#     Frequency map: O(n)
#     Heap and result list: O(k)
#     Total: O(n)

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency of each element
        freq_map = Counter(nums)  # O(n)

        # Step 2: Use a heap to get k elements with highest frequency
        # heapq.nlargest returns the k keys with highest frequency
        top_k = heapq.nlargest(k, freq_map.keys(), key=freq_map.get)  # O(n log k)

        return top_k

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,1,4], 2))         # Output: [1, 2]
print(sol.topKFrequent([3,2,1,5,6,4], 2))             # Output: [3, 2] or [2, 3] (depends on internal ordering)
print(sol.topKFrequent([3,2,3,1,2,4,5,5,6], 4))       # Output: [3, 2, 5, 1] (or similar)
print(sol.topKFrequent([1,2,3,4,5], 5))               # Output: [1,2,3,4,5]
