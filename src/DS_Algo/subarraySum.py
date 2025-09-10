# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

# Time:  O(n) We traverse the array once..
# Space:  O(n) We store prefix sums in a hashmap.

# Explanation:
# To solve the problem of finding the total number of subarrays whose sum equals k, we can use a prefix sum + hashmap approach for optimal performance.
    # Let prefix_sum be the running sum of elements.
    # If prefix_sum - k has been seen before, it means there's a subarray ending at the current index that sums to k.
    # We use a hashmap (prefix_map) to store the frequency of each prefix sum.

# sum(i,j)=sum(0,j)−sum(0,i) - This means:
    # If we know the sum from 0 to j (prefix_sum)
    # And we know the sum from 0 to i (prefix_sum - k)
    # Then the subarray from i to j sums to k.


from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # Base case: sum 0 occurs once

        for num in nums:
            prefix_sum += num
            count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] += 1

        return count


# Create an instance of the class
sol = Solution()

nums = [1, 1, 1]
k = 2
output = sol.subarraySum(nums, k)
# Output: 2 → subarrays [1,1] at indices (0,1) and (1,2)
