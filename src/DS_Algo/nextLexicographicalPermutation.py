# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
#  More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
#  then the next permutation of that array is the permutation that follows it in the sorted container. 
#  If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

# Time Complexity:
# Worst case:  O(n)
#     Finding the pivot: O(n)
#     Finding the successor: O(n)
#     Reversing the suffix: O(n)

# Space Complexity: O(1) (in-place modification, no extra space used)

# Logic:

# 1. Find the pivot: Traverse from the end to find the first index i where nums[i] < nums[i + 1]. 
#   This marks the point where the next permutation can be formed.
# 2. Find the successor: From the end again, find the first index j such that nums[j] > nums[i].
# 3. Swap: Swap nums[i] and nums[j].
# 4. Reverse the suffix: Reverse the subarray from i + 1 to the end to get the next smallest lexicographical order.

# If no such i is found (i.e., the array is in descending order), the array is the last permutation. 
#   So we reverse the entire array to get the first permutation.


from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to its next lexicographical permutation.
        If no such permutation exists, rearranges to the lowest possible order.
        """
        n = len(nums)

        # Step 1: Find the first decreasing element from the end
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the smallest number greater than nums[i] to the right of i
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray from i+1 to the end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Create an instance of the class
sol = Solution()

# Call the method with an input list
# Already lowest permutation	[1,2,3]	output: [1,3,2]
# Already highest permutation : [3,2,1]	 output: [1,2,3]
# Duplicates	[1,1,5]	output: [1,5,1]
# Single element	[1]	output: [1]
# Two elements	[2,1]	output: [1,2]
# All elements equal	[5,5,5]	output: [5,5,5]
nums = [1, 2, 3]

sol.nextPermutation(nums)

# Print the result
print(nums)  # Output: [1, 3, 2]

