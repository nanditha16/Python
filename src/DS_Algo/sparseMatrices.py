# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, 
# return the result of mat1 x mat2. You may assume that multiplication 
# is always possible.

# Example:
# Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# Output: [[7,0,0],[-7,0,3]]

# Input: mat1 = [[0]], mat2 = [[0]]
# Output: [[0]]
 
# Constraints:
#     m == mat1.length
#     k == mat1[i].length == mat2.length
#     n == mat2[i].length
#     1 <= m, n, k <= 100
#     -100 <= mat1[i][j], mat2[i][j] <= 100

# Step-by-Step Explanation
# Example:
#     mat1 = [[1, 0, 0], [-1, 0, 3]]
#     mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
# Step 1: Preprocess mat1
# Store only non-zero entries:
#     mat1_map = {    0: [(0, 1)],    1: [(0, -1), (2, 3)]}
# Step 2: Preprocess mat2
#     Store only non-zero entries:
#     mat2_map = {    0: [(0, 7)],    2: [(2, 1)]}
# Step 3: Multiply
# Iterate over non-zero entries only:
#     For row 0 in mat1, use value at column 0 → multiply with row 0 in mat2
#     1 * 7 = 7 → result[0][0] = 7
#     For row 1 in mat1, use values at columns 0 and 2
#     -1 * 7 = -7 → result[1][0] = -7
#     3 * 1 = 3 → result[1][2] = 3

# Final Result:[[7, 0, 0], [-7, 0, 3]]


# Edge Case Handling
#     Zero matrices: Skips zero entries to optimize performance.
#     Dimension mismatch: Raises an error if multiplication is not possible.
#     Single element matrices: Works correctly for 1×1 matrices.
#     Sparse optimization: Only processes non-zero values.

# Time Complexity
# Preprocessing: O(mk+kn)
# Multiplication: Only non-zero entries → efficient for sparse matrices
# Worst case: O(m⋅k⋅n) (dense matrices)
# Best case: Much less for sparse matrices

# Space Complexity
# Maps for non-zero entries: O(non-zero entries)
# Result matrix: O(m⋅n)

class Solution:
    def sparseMatricesMultiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        k2, n = len(mat2), len(mat2[0])
        
        # Edge case: ensure dimensions match for multiplication
        if k != k2:
            raise ValueError("Matrix dimensions do not allow multiplication")

        # Step 1: Preprocess mat1 to store non-zero entries
        mat1_map = {}
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    mat1_map.setdefault(i, []).append((j, mat1[i][j]))

        # Step 2: Preprocess mat2 to store non-zero entries
        mat2_map = {}
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    mat2_map.setdefault(i, []).append((j, mat2[i][j]))

        # Step 3: Multiply using only non-zero entries
        result = [[0] * n for _ in range(m)]
        for i in mat1_map:
            for a_col, a_val in mat1_map[i]:
                if a_col in mat2_map:
                    for b_col, b_val in mat2_map[a_col]:
                        result[i][b_col] += a_val * b_val

        return result
    