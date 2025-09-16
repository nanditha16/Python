# Given an integer array nums and an integer k, 
# return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Can you solve it without sorting?

# Constraints:
# 1 <= k <= nums.length <= 10^5
# -104 <= nums[i] <= 10^4

# Example:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Step-by-Step Explanation
# 1. Initialize a Min-Heap with the first k elements.
#     This heap will store the k largest elements seen so far.
#     The smallest among them (i.e., the root) is the current kth largest.
# 2. Iterate through the rest of the array:
#     If the current number is larger than the smallest in the heap, it belongs in the top k.
#     Replace the smallest using heappushpop() for efficiency.
# 3. Return the root of the heap:
#     After processing all elements, the root is the kth largest.

# Edge Case Coverage
#     k = 1 → returns the largest element
#     k = len(nums) → returns the smallest element
#     Duplicates → handled correctly
#     Negative numbers → handled correctly
#     Large arrays (up to 10⁵ elements) → efficient

# Time Complexity: O(n log k)
#     n = number of elements in nums
#     Heap operations (heapify, heappushpop) are O(log k)
#     We process each of the n - k remaining elements → total time is O(n log k)
# Space Complexity: O(k)
#     The heap stores only k elements

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Maintain a min-heap of size k
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
