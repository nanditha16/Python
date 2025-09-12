# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result
#  in any order.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Time Complexity: O(n+m) Where n and m are the lengths of nums1 and nums2.
# Space Complexity: O(n+m) For storing the sets.

# Example:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# Step-by-Step Explanation
# 1. Convert both arrays to sets:
#     This removes duplicates and allows efficient set operations.
#     Example: nums1 = [1,2,2,1] → set1 = {1,2}
# 2. Find the intersection:
#     Use set1 & set2 to get common elements.
#     Example: set1 = {1,2}, set2 = {2} → intersection = {2}
# 3. Convert the result to a list:
#     Final output: [2]

# Edge Case Handling
#     Arrays with no common elements → returns []
#     Arrays with all elements in common → returns unique elements only
#     Empty arrays → returns []

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        # Return the intersection as a list
        return list(set1 & set2)
