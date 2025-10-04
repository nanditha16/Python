# Given an integer array nums with possible duplicates, 
# randomly output the index of a given target number. 
# You can assume that the given target number must exist in the array.

# Implement the Solution class:
#     Solution(int[] nums) Initializes the object with the array nums.
#     int pick(int target) Picks a random index i from
#      nums where nums[i] == target. If there are multiple valid i's, 
#      then each index should have an equal probability of returning.
    

# Example:

# Input
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# Output
# [null, 4, 0, 2]

# Explanation
# Solution solution = new Solution([1, 2, 3, 3, 3]);
# solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 
# Constraints:
#     1 <= nums.length <= 2 * 10^4
#     -2^31 <= nums[i] <= 2^31 - 1
#     target is an integer from nums.
#     At most 10^4 calls will be made to pick.

# Edge Case Handling
#     Duplicates: Handled by storing all indices of each number.
#     Single occurrence: random.choice() works even if there's only one index.
#     Guaranteed existence: As per constraints, the target always exists in nums, so no need to check for missing keys.
#     Large input size: Efficient due to preprocessing.

# Step-by-Step Explanation
# 1. Initialization (__init__ method)
#     Create a dictionary indices_map where:
#     Key: number from nums
#     Value: list of all indices where that number appears
# 2. Picking (pick method)
#     When pick(target) is called:
#     Retrieve the list of indices for target from indices_map
#     Use random.choice() to randomly select one index from the list

# Time Complexity
#     Initialization: O(n)— one pass through nums to build the map
#     Pick operation: O(1)— dictionary lookup and random selection

# Space Complexity
#     Storage: O(n)— storing all indices in a dictionary

class Solution:

    def __init__(self, nums):
        # Step 1: Preprocess the array to store indices of each number
        self.indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices_map[num].append(i)

    def pick(self, target):
        # Step 2: Randomly pick one index from the list of indices for the target
        return random.choice(self.indices_map[target])

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)