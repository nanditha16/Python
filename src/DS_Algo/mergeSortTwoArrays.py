
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
# should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

# Time Complexity: O(m+n) Each element is visited once
# Space Complexity: O(1) In-place merge, no extra space used

# Let’s walk through the example:
#     Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

# Step 1: Use three pointers
#     i = m - 1 = 2 → points to last valid element in nums1
#     j = n - 1 = 2 → points to last element in nums2
#     k = m + n - 1 = 5 → points to last position in nums1
# Step 2: Compare and place larger element at the end
#     Compare nums1[i] and nums2[j]
#     Place the larger at nums1[k]
#     Move pointers accordingly
# Step 3: Copy remaining elements from nums2 (if any)
#     f nums2 still has elements, copy them to nums1
#     Output: nums1 = [1,2,2,3,5,6]

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of both arrays
        i = m - 1  # Last element in nums1's actual data
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last position in nums1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements left in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Create an instance of the class
sol = Solution()

# Input arrays
nums1 = [-1, 2, 3, 0, 0, 0]
m = 3
nums2 = [-2, 5, 6]
n = 3

# Call the method with all required arguments
sol.merge(nums1, m, nums2, n)

# Print the result
print(nums1)
