
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. 
# If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element 
# is always considered to be strictly greater than a neighbor that is outside
#  the array.

# You must write an algorithm that runs in O(log n) time.

# Constraints:
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.

# Time Complexity: O(logn) — binary search.
# Space Complexity: O(1) — constant space.

# Example:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 
# where the peak element is 2, or index number 5 where the peak element is 6.

# Step-by-Step Explanation
# 1. Binary search is used to find a peak efficiently.
# 2. At each step:
#     Compare nums[mid] with nums[mid + 1].
#     If nums[mid] > nums[mid + 1], the peak is on the left side (including mid).
#     Otherwise, the peak is on the right side.
# 3. The loop continues until left == right, which is the peak index.

# Edge Case Handling
#     Single element → it's a peak.
#     Peak at the beginning or end of the array.
#     Multiple peaks → returns any one of them (as allowed).

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # Peak is on the left side (including mid)
                right = mid
            else:
                # Peak is on the right side
                left = mid + 1

        return left  # or right, since left == right