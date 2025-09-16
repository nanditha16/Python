# A row-sorted binary matrix means that all elements are 0 or 1 and 
# each row of the matrix is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return the index
#  (0-indexed) of the leftmost column with a 1 in it.
#   If such an index does not exist, return -1.

# You can't access the Binary Matrix directly. You may only
#  access the matrix using a BinaryMatrix interface:

# - BinaryMatrix.get(row, col) returns the element of the matrix at 
# index (row, col) (0-indexed).
# - BinaryMatrix.dimensions() returns the dimensions of the matrix 
# as a list of 2 elements [rows, cols], which means the matrix 
# is rows x cols.
# Submissions making more than 1000 calls to BinaryMatrix.get 
# will be judged Wrong Answer. Also, any solutions that attempt
#  to circumvent the judge will result in disqualification.

# For custom testing purposes, the input will be the entire
#  binary matrix mat. You will not have access to the binary 
#  matrix directly.

# Constraints:
#     rows == mat.length
#     cols == mat[i].length
#     1 <= rows, cols <= 100
#     mat[i][j] is either 0 or 1.
#     mat[i] is sorted in non-decreasing order.

# Example: 
# Input: mat = [[0,0],[1,1]]
# Output: 0

# Input: mat = [[0,0],[0,1]]
# Output: 1

# Input: mat = [[0,0],[0,0]]
# Output: -1
 
# leftmost column with at least one 1 in a row-sorted binary matrix,
#  using the BinaryMatrix interface.

# Step-by-Step Explanation
# 1. Start at the top-right corner of the matrix:
#     This position allows us to move left when we find a 1 and down when we find a 0.
# 2. Traverse the matrix:
#     If the current cell is 1, it means there might be a 1 further left in the same row → move left.
#     If the current cell is 0, it means this column has no 1 in this row → move down.
# 3. Track the leftmost column:
#     Every time we find a 1, we update the leftmost variable.
# 4. Stop when:
#     We either reach the bottom row or move past the first column.
# 5. Return the result:
#     If we found any 1, return its column index.
#     Otherwise, return -1.

# Time Complexity: O(rows + cols)
#     Each step moves either left or down.
#     At most rows + cols steps are made.
# Space Complexity: O(1)
#     No extra space used beyond a few variables.

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
   def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get the dimensions of the matrix
        rows, cols = binaryMatrix.dimensions()

        # Start from the top-right corner
        row, col = 0, cols - 1

        # Track the leftmost column with a 1
        leftmost = -1

        # Traverse the matrix
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                # Found a 1, update leftmost and move left
                leftmost = col
                col -= 1
            else:
                # Found a 0, move down to the next row
                row += 1

        return leftmost
