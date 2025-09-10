# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Time Complexity: O(n) — two linear passes.
# Space Complexity:O(1) extra space if we don't count the output array.
# Otherwise, O(n) for the output.

# Explanation
# Prefix pass: For each index i, store the product of all elements before i.
# Suffix pass: Traverse from the end and multiply each element with the product of all elements after i.
# This avoids using division and ensures each element is the product of all others.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Step 1: Compute prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Compute suffix products and multiply with prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

sol = Solution()

print(sol.productExceptSelf([1, 2, 3, 4]))       # Output: [24, 12, 8, 6]
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
