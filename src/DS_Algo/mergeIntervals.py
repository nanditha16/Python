# Given an array of intervals where intervals[i] = [starti, endi],
#  merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4

# Time Complexity: O(nlogn) — due to sorting
# Space Complexity: O(n) — for storing the merged intervals

# Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.

# Step-by-Step Explanation
# 1. Sort the intervals by their start time to ensure we process them in order.
# 2. Initialize the merged list with the first interval.
# 3. For each subsequent interval:
#     If it overlaps with the last interval in merged, merge them by updating the end time.
#     Otherwise, append it as a new non-overlapping interval.

# Edge Case Handling
#     Empty input list → returns []
#     Single interval → returns the same interval
#     Fully overlapping intervals → merged into one
#     Touching intervals (e.g., [1,4] and [4,5]) → considered overlapping

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # Step 2: Iterate and merge overlapping intervals
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # Overlap
                last[1] = max(last[1], current[1])  # Merge
            else:
                merged.append(current)

        return merged
