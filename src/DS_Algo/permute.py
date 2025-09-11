# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# Time	O(n!)	There are n! permutations
# Space	O(n)	Recursion stack depth is n

# Example:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Input: nums = [1]
# Output: [[1]]

# Method 1: Step-by-Step Explanation
# Backtracking:
#     We use recursion to explore all possible positions for each element.
#     At each level, we swap the current element with every other element that hasn't been fixed yet.
# Base Case:
#     When start == len(nums), we've formed a complete permutation → add a copy to result.
# Swap and Backtrack:
#     Swap elements to fix one at the current position.
#     Recurse to fix the next position.
#     Swap back to restore the original state (backtracking).

# Method 2: How It Works
# Initialization:
#     res: stores all permutations.
#     used: tracks which elements are already in the current path.
#     path: builds the current permutation.
# DFS Function:
#     Base case: if path has n elements, it's a complete permutation → add a copy to res.
#     Recursive case: iterate through nums, skip used elements, choose one, recurse, then backtrack.
# Backtracking:
#     After exploring a path, undo the choice (pop and used[i] = False) to explore other paths.

# Method 3: Permutations II - Given a collection of numbers, nums, that might contain duplicates,
#  return all possible unique permutations in any order.

# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# Time	O(n × n!)	Worst-case with all unique elements
# Space	O(n)	Recursion depth and used array

# Example:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Step-by-Step Explanation
# Sort the input list:
#     Ensures duplicates are adjacent, which helps in skipping them.
# Use backtracking:
#     Build permutations recursively.
#     Track used elements with a used array.
# Skip duplicates:
#     If nums[i] == nums[i - 1] and nums[i - 1] was not used in this path, skip nums[i].
# Build and backtrack:
#     Add element to path, recurse, then remove it and mark as unused.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])  # Make a copy of the current permutation
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        backtrack()
        return result

    def permuteNoInplaceSwaps(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res: List[List[int]] = []
        used = [False] * n
        path: List[int] = []

        def dfs():
            if len(path) == n:
                res.append(path[:])        # copy the current permutation
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True             # choose
                path.append(nums[i])
                dfs()                      # explore
                path.pop()                 # un-choose
                used[i] = False

        dfs()
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to handle duplicates
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: only use the first occurrence
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res
