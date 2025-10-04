# An array is monotonic if it is either monotone increasing or 
# monotone decreasing.

# An array nums is monotone increasing if for all i <= j, 
# nums[i] <= nums[j]. An array nums is monotone decreasing 
# if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic,
#  or false otherwise.

# Example:
# Input: nums = [1,2,2,3]
# Output: true

# Input: nums = [6,5,4,4]
# Output: true

# Input: nums = [1,3,2]
# Output: false
 
# Constraints:
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5

# Time Complexity: O(n) — single pass through the array
# Space Complexity: O(1) — only uses two boolean flags

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False

        return increasing or decreasing


sol = Solution()
print(sol.isMonotonic([1, 2, 2, 3]))     # True
print(sol.isMonotonic([6, 5, 4, 4]))     # True
print(sol.isMonotonic([1, 3, 2]))        # False
print(sol.isMonotonic([1]))              # True
print(sol.isMonotonic([1, 1, 1]))        # True

