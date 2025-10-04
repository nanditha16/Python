# Given an integer array nums and an integer k, 
# find three non-overlapping subarrays of length k with maximum 
# sum and return them.

# Return the result as a list of indices representing the starting 
# position of each interval (0-indexed). If there are multiple answers,
#  return the lexicographically smallest one.

# Example:
# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4]
 

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)

# Edge Case Handling
#     Minimum size: Works when len(nums) = 3 * k
#     Multiple answers: Uses >= in right selection to ensure lexicographically smallest
#     All zeros or same values: Still returns correct indices
#     Large input: Efficient due to linear preprocessing

# Step-by-Step Explanation
# Example: nums = [1,2,1,2,6,7,5,1], k = 2
# Step 1: Compute sums of all subarrays of length k
#     window_sum = [3, 3, 3, 8, 13, 12, 6]
# Step 2: Track best left and right indices
#     left[i] stores index of max sum from 0 to i
#     right[i] stores index of max sum from i to end
#     left =  [0, 0, 0, 3, 4, 4, 4]right = [4, 4, 4, 4, 4, 5, 6]
# Step 3: Try all middle intervals
#     For each mid in range [k, len(window_sum) - k]
#     Get left[mid - k] and right[mid + k]
#     Compute total and update result if better
# Best combination:
#     left = 0, mid = 3, right = 5 → sums = 3 + 8 + 12 = 23
# Final Output: [0, 3, 5]

# Time Complexity: Total:  O(n)
#     Prefix sums: O(n)
#     Left/right tracking: O(n)
#     Final scan: O(n)
# Space Complexity : Total: O(n)
#     window_sum, left, right: O(n)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # Step 1: Compute prefix sums for all subarrays of length k
        window_sum = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sum[0] = curr_sum
        for i in range(1, n - k + 1):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr_sum

        # Step 2: Track best left and right positions for each middle index
        left = [0] * len(window_sum)
        best_left = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best_left]:
                best_left = i
            left[i] = best_left

        right = [0] * len(window_sum)
        best_right = len(window_sum) - 1
        for i in reversed(range(len(window_sum))):
            if window_sum[i] >= window_sum[best_right]:  # >= for lexicographical order
                best_right = i
            right[i] = best_right

        # Step 3: Try all middle intervals and find max total
        max_total = 0
        result = []
        for mid in range(k, len(window_sum) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = window_sum[l] + window_sum[mid] + window_sum[r]
            if total > max_total:
                max_total = total
                result = [l, mid, r]

        return result
