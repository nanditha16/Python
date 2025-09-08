# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Constraints:

# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# Logic:
# The array is sorted, so duplicates are adjacent.
# k keeps track of the next position to place a unique element.
# If nums[i] != nums[k - 1], it means nums[i] is a new unique value.
# We overwrite nums[k] with nums[i] and increment k.

# Time Complexity: O(n)
    # The loop runs from i = 1 to len(nums) - 1, so it iterates once per element in the array.
    # Each operation inside the loop is constant time: comparisons, assignments, and increments.
    # Therefore, the total time complexity is linear, or O(n), where n is the length of the input list nums.

# Space Complexity: O(1)
    # No additional data structures are used.
    # The algorithm modifies the input list in-place.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for the position of the next unique element
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    


sol = Solution()

# Test case
nums = [1, 1, 2, 2, 3]
expectedNums = [1, 2, 3]

k = sol.removeDuplicates(nums)

# Assertions
assert k == len(expectedNums), f"Expected length {len(expectedNums)}, got {k}"
for i in range(k):
    assert nums[i] == expectedNums[i], f"Mismatch at index {i}: expected {expectedNums[i]}, got {nums[i]}"

print("Test passed!")
