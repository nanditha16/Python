# Given an integer array nums and an integer k, return true if nums has
#  a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.

# Note that:
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n 
# such that x = n * k. 0 is always a multiple of k.

# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1

# Example:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

# Step-by-Step Explanation
# 1. Prefix Sum:
#     Keep a running total of the sum of elements.
# 2. Modulo Trick:
#     If two prefix sums have the same remainder when divided by k, the subarray between them is a multiple of k.
# 3. HashMap (remainder_map):
#     Stores the first index where each remainder occurred.
#     Initialized with {0: -1} to handle cases where the subarray starts from index 0.
# 4. Check Subarray Length:
#     Ensure the subarray length is at least 2: i - prev_index >= 2.

# Edge Case Handling
#     k == 0: handled by skipping modulo and using raw sum.
#     Subarray must be at least length 2.
#     Works even if nums contains zeros.

# Time Complexity: O(n) — single pass through the array.
# Space Complexity: O(k) — hashmap stores remainders (bounded by k).

# Example Walkthrough
# Input: nums = [23, 2, 4, 6, 7], k = 6
#     Prefix sums: [23, 25, 29, 35, 42]
#     Remainders: [5, 1, 5, 5, 0]
#     When remainder 5 repeats at index 2 and 0, subarray [2, 4] is valid.


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: -1}  # Initialize with mod 0 at index -1 to handle edge cases
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:
                cumulative_sum %= k  # Only take mod if k is not zero

            if cumulative_sum in mod_map:
                if i - mod_map[cumulative_sum] > 1:  # Ensure subarray length is at least 2
                    return True
            else:
                mod_map[cumulative_sum] = i  # Store the first occurrence of this mod value

        return False