# You are given two lists of closed intervals, firstList and secondList,
#  where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
#  Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real 
# numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers 
# that are either empty or represented as a closed interval. For example, 
# the intersection of [1, 3] and [2, 4] is [2, 3].

# Example:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []


# Constraints:
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109
# endj < startj+1

# Step-by-Step Explanation
# 1. Initialize two pointers i and j for firstList and secondList.
# 2. Loop while both pointers are within bounds.
# 3. For each pair of intervals:
#     Extract [start1, end1] and [start2, end2].
#     Check if they overlap using:
#         start1 <= end2 and start2 <= end1
# 4. If they overlap:
#     Compute the intersection:
#         start = max(start1, start2)
#         end = min(end1, end2)
#     Append [start, end] to the result.
# 5. Move the pointer that has the smaller end time to avoid missing future overlaps.
# 6. Continue until one list is fully traversed.

# Let: n=len(firstList), m=len(secondList)
# Time Complexity: O(n+m) — each interval is processed once.
# Space Complexity: O(k) — where k is the number of intersections (output size).

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        intersections = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            # Check if intervals overlap
            if start1 <= end2 and start2 <= end1:
                # Calculate the intersection
                start = max(start1, start2)
                end = min(end1, end2)
                intersections.append([start, end])

            # Move to the next interval in the list that ends first
            if end1 < end2:
                i += 1
            else:
                j += 1

        return intersections