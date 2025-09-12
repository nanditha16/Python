# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an 
# unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], 
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and 
# become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target,
#  return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Constraints:
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4

# Time Complexity: O(logn) — binary search.
# Space Complexity: O(1) — constant space.

# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Input: nums = [1], target = 0
# Output: -1

# Step-by-Step Explanation
# 1. Use binary search with two pointers: left and right.
# 2. Calculate mid and check if nums[mid] == target.
# 3. Determine which half of the array is sorted:
#     If nums[left] <= nums[mid], the left half is sorted.
#     Otherwise, the right half is sorted.
# 4. Decide whether to search left or right based on where the target could lie.
# 5. Repeat until the target is found or the search space is exhausted.

# Edge Case Handling
#     Array with one element.
#     Target not present.
#     Target is at the rotation point.
#     Fully sorted array (no rotation).
#     Rotation at the first or last index.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1   # Target is in the right half
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right half
                else:
                    right = mid - 1  # Target is in the left half

        return -1
