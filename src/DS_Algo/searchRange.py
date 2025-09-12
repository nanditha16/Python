# Given an array of integers nums sorted in non-decreasing order,
#  find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9

# Time Complexity: O(logn) — binary search twice.
# Space Complexity: O(1) — no extra space used.

# Example:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Input: nums = [], target = 0
# Output: [-1,-1]

# Step-by-Step Explanation
# 1. Use binary search twice:
#     First to find the leftmost (first) index of the target.
#     Second to find the rightmost (last) index of the target.
# 2. In each search:
#     If nums[mid] == target, update the bound and continue searching in the appropriate half.
#     If nums[mid] < target, move left pointer.
#     If nums[mid] > target, move right pointer.
# 3. If the target is not found, both searches return -1.

# Edge Case Handling
#     Empty array → returns [-1, -1]
#     Target not present → returns [-1, -1]
#     Target appears once → returns [i, i]
#     Target appears multiple times → returns [first_index, last_index]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_left):
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        right = mid - 1  # Search left half
                    else:
                        left = mid + 1   # Search right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        start = find_bound(True)
        end = find_bound(False)
        return [start, end]
