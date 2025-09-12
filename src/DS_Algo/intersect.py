# Given two integer arrays nums1 and nums2, return an array of their intersection.
#  Each element in the result must appear as many times as it shows 
#  in both arrays and you may return the result in any order.

# Follow up:
# What if the given array is already sorted? How would you optimize 
# your algorithm?
# What if nums1's size is small compared to nums2's size? 
# Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited
#  such that you cannot load all elements into the memory at once?

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Example:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Method 1: Counter-based 
# Step-by-Step Explanation
# 1. Use Counter from collections to count the frequency of each number in both arrays.
# 2. For each number in nums1, check if it exists in nums2.
# 3. If it does, add it to the result min(count1[num], count2[num]) times.
# 4. Return the result list.

# Time Complexity: O(n+m) Where n and m are the lengths of nums1 and nums2.
# Space Complexity: O(n+m) For storing the frequency maps.

# Methos 2: Follow-Up Optimizations - two-pointer version for sorted arrays
# 1. If arrays are sorted: 
#     Use two pointers to traverse both arrays in linear time.
#     Avoid using extra space.

#  Step-by-Step Explanation
# 1. Sort both arrays (if not already sorted).
# 2. Initialize two pointers i and j at the start of nums1 and nums2.
# 3. Traverse both arrays:
#     If nums1[i] == nums2[j], it's a match → add to result and move both pointers.
#     If nums1[i] < nums2[j], move i forward.
#     If nums1[i] > nums2[j], move j forward.
# 4. Continue until one pointer reaches the end.

# Time Complexity: O(nlogn+mlogm) for sorting, O(n+m) for traversal→ Total: O(nlogn+mlogm)
# Space Complexity: O(1) extra space (excluding result)

# Methos 3: Follow-Up Optimizations  - disk-based streaming approach
# 1. If nums1 is much smaller than nums2: disk-based streaming
#     Build a frequency map for the smaller array to reduce memory usage.
#     Stream through the larger array and match elements.
# 2. If nums2 is stored on disk and memory is limited:
#     Load nums2 in chunks.
#     Use a frequency map for nums1 in memory.
#     For each chunk of nums2, compute the intersection and update the result.

# Problem Setup
#     nums1 fits in memory.
#     nums2 is stored on disk and must be processed in chunks.
#     Goal: return the intersection, including duplicates, where each element appears as many times as it occurs in both arrays.

# Strategy
# 1. Load nums1 into memory and build a frequency map using collections.Counter.
# 2. Stream nums2 from disk in chunks (e.g., 1000 elements at a time).
# 3. For each chunk:
#     Check each element against the frequency map.
#     If it exists and count > 0, add it to the result and decrement the count.
# 4. Continue until all chunks are processed.

# Time Complexity: O(n+m) — where n is size of nums1, m is total elements in nums2.
# Space Complexity:O(n) — for storing frequency map of nums1.

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count frequencies in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # Find intersection with minimum frequency
        result = []
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))

        return result
    
    def intersectTwoPointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both arrays (if not already sorted)
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []

        # Use two pointers to traverse both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

    # Python Pseudocode
    def intersect_streaming(self, nums1, nums2_stream):
        count1 = Counter(nums1)
        result = []

        for chunk in nums2_stream:  # Simulate reading from disk
            for num in chunk:
                if count1[num] > 0:
                    result.append(num)
                    count1[num] -= 1

        return result
    
    # Simulate nums2_stream Pseudocode
    def read_chunks_from_disk(self, file_path, chunk_size=1000):
        with open(file_path) as f:
            chunk = []
            for line in f:
                chunk.append(int(line.strip()))
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk
