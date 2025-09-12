# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check.
#  Since each version is developed based on the previous version,
#   all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
# bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether 
# version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

# Constraints:
# 1 <= bad <= n <= 2^31 - 1

# Time Complexity: O(logn) — binary search.
# Space Complexity: O(1) — constant space.

# Example:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Input: n = 1, bad = 1
# Output: 1

# Step-by-Step Explanation
#     Binary search narrows the range by half each time.
#     We only call isBadVersion(mid) once per iteration.
#     We stop when low == high, which must be the first bad version.

# Let’s walk through an example:
# Input: n = 5, bad = 4
# Versions: [1, 2, 3, 4, 5]
# isBadVersion(4) and isBadVersion(5) return True
# isBadVersion(1-3) return False

#     Iteration 1:
#         low = 1, high = 5
#         mid = 1 + (5 - 1) // 2 = 3
#         isBadVersion(3) → False
#         So, the first bad version must be after 3 → low = 4
#     Iteration 2:
#         low = 4, high = 5
#         mid = 4 + (5 - 4) // 2 = 4
#         isBadVersion(4) → True
#         So, the first bad version is at or before 4 → high = 4
#     Exit:
#       low == high == 4 → return 4

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n

        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid  # mid might be the first bad version
            else:
                low = mid + 1  # first bad version must be after mid

        return low  # or high, since low == high

