# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Follow up: Could you minimize the total number of operations done?

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Time Complexity: O(n)
# Space Complexity: O(1) (in-place)


# Method 1: Two pass - moveZeroes
# Complexity:
# Time: O(n)
# Space: O(1)
# Writes: Up to n writes (non-zero + zero fill) - May write the same value twice (e.g., nums[i] = nums[i]).

# Explanation
# To solve the "Move Zeroes" problem in-place and minimize operations, we can use a two-pointer approach:
    # First pass: Move all non-zero elements to the front of the array.
    # Second pass: Fill the remaining positions with zeroes.
# This approach ensures:
#     In-place modification
#     Preserves relative order
#     Minimizes operations (each element is moved at most once)

# Method 2: One-Pass with Swapping - moveZeroesOnePass
# Complexity:
# Time: O(n)
# Space: O(1)
# Swaps: Fewer than n, but each swap is 2 writes. - Swapping involves 2 writes per operation, which may be more costly than direct assignment.
 
# Explanation:
# Swaps non-zero elements forward in a single pass.
# Avoids self-swaps with if i != last_non_zero.

# Method 3: Optimized Writes - moveZeroesFewerWritesThanSwapping
# Complexity:
# Time: O(n)
# Space: O(1)
# Writes: Minimal — only when necessary.

# Explanation:
# Moves non-zero elements forward.
# Sets zero only when needed.
# Avoids unnecessary swaps and self-writes.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0  # Position to place the next non-zero element

        # First pass: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # Second pass: fill the rest with zeroes
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0

    # Go with this, less complex hence better runtime 
    def moveZeroesOnePass(self, nums: List[int]) -> None:
        """
        Move all zeros to the end while keeping the relative order of non-zeros.
        One pass, O(1) extra space.
        """
        last_non_zero = 0  # Position to place the next non-zero element
        
        # First pass: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != last_non_zero:                # avoid self-swap
                    nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1

    
    def moveZeroesFewerWritesThanSwapping(self, nums: List[int]) -> None:
        last_non_zero = 0 # Position to place the next non-zero element

        # First pass: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                if i != last_non_zero:  # avoid self-swap
                    nums[i] = 0
                last_non_zero += 1

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

Solution().moveZeroesOnePass(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

Solution().moveZeroesFewerWritesThanSwapping(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
      