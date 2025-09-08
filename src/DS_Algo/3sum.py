# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Constraints:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

# Logic:

# Time Complexity: O(n²) and Space Complexity: O(1) (excluding output list) . 
                   
# 1. Sort the array to make it easier to avoid duplicates and use two pointers.
# 2. Iterate through the array, fixing one number (nums[i]) at a time.
# 3. Use two pointers (left and right) to find pairs that sum with nums[i] to zero.
# 4. Skip duplicates to ensure only unique triplets are added.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         # Sort the array to make it easier to avoid duplicates and use two pointers.
        nums.sort()
        result = []
        n = len(nums)

        # Iterate through the array, fixing one number (nums[i]) at a time.
        for i in range(n):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Use two pointers (left and right) to find pairs that sum with nums[i] to zero.
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result