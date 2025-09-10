# Given an m x n 2D binary grid grid which represents a map of '1's (land)
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of 
# the grid are all surrounded by water.

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.

# Example:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Methos 1: Explanation:
# To solve the Number of Islands problem, we can use Depth-First Search (DFS)
# or Breadth-First Search (BFS) to explore each island and mark visited land cells.

# Given:
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# Start scanning from top-left.
# First '1' found at (0,0) → start DFS → mark all connected '1's → island #1
# Continue scanning → next '1' at (2,2) → start DFS → island #2
# Next '1' at (3,3) → start DFS → includes (3,4) → island #3
# Done scanning → return 3

# Time Complexity: O(m×n) — each cell is visited once
# Space Complexity: DFS recursion stack: O(m × n) in worst case (all land)
# Can be reduced using iterative BFS


# Method 2:
# Step-by-Step Explanation
# 1. Check for empty grid: If the grid is empty or has no columns, return 0.
# 2. Initialize dimensions: R and C are the number of rows and columns.
# 3. Iterate through each cell:
#     If a cell contains '1', it's part of an island.
#     Increment the island count.
#     Use BFS (deque) to traverse all connected '1's.
# 4. BFS traversal:
#     Mark the current cell as visited by setting it to '0'.
#     Add its neighbors (up, down, left, right) to the queue if they are '1'.
#     Continue until all connected land is visited.
# 5. Return the count of islands.

# Time Complexity: O(R × C)
#     Each cell is visited once.
#     BFS explores each '1' cell and marks it as '0'.
#     So total operations are proportional to the number of cells.
# Space Complexity: O(min(R, C))
#     In the worst case, the queue can hold all cells of one island.
#     For a narrow island (e.g., a vertical strip), the queue size 
#     is proportional to the smaller dimension.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # Mark as visited
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count

    def numIslandsIterative(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        R, C = len(grid), len(grid[0])
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    q = deque([(r, c)])
                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                q.append((nx, ny))
        return count
