# You are given an m x n grid grid of values 0, 1, or 2, where:
#     each 0 marks an empty land that you can pass by freely,
#     each 1 marks a building that you cannot pass through, and
#     each 2 marks an obstacle that you cannot pass through.
# You want to build a house on an empty land that reaches all buildings 
# in the shortest total travel distance. You can only move up, down, left, 
# and right.

# Return the shortest travel distance for such a house. If it is not 
# possible to build such a house according to the above rules, return -1.

# The total travel distance is the sum of the distances between the 
# houses of the friends and the meeting point.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0, 1, or 2.
# There will be at least one building in the grid.

# Time Complexity: O(m × n × b)
#     b = number of buildings
#     For each building, BFS traverses up to m × n cells
# Space Complexity: O(m × n)
#     For total_dist, reach_count, and visited matrices

# Example:
# Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7
# Explanation: Given three buildings at (0,0), (0,4), (2,2),
#  and an obstacle at (0,2).
# The point (1,2) is an ideal empty land to build a house, as 
# the total travel distance of 3+3+1=7 is minimal.
# So return 7.

# Input: grid = [[1,0]]
# Output: 1

# Input: grid = [[1]]
# Output: -1

# METHOD 1: 
# Step-by-Step Explanation
# Initialize:
#     total_dist[i][j]: total distance from all buildings to cell (i,j)
#     reach_count[i][j]: number of buildings that can reach cell (i,j)
#     building_count: total number of buildings
# BFS from each building:
#     For each building cell (i,j), perform BFS.
#     For each reachable empty land (x,y), update:
#         total_dist[x][y] += distance
#         reach_count[x][y] += 1
# Find minimum distance:
#     Iterate over all empty lands.
#     If reach_count[i][j] == building_count, it's reachable from all buildings.
#     Track the minimum total_dist[i][j].
# Return result:
#     If no cell is reachable from all buildings, return -1.
#     Otherwise, return the minimum distance.

# METHOD 2: 
# Step-by-Step Explanation
# 1. Keep a single dist[R][C] matrix for summed distances.
# 2. Reuse the input grid to mark which empty cells are still eligible.
# Use an integer walk starting at 0. An empty cell is visitable in the current BFS only if grid[r][c] == walk. When you visit it, set grid[r][c] = walk - 1.
# After finishing BFS for one building, do walk -= 1.
# → This guarantees that in later BFS runs you only traverse cells that were reachable from all previous buildings—no extra visited matrix and far fewer pushes.
# 3. At the end, cells with grid[r][c] == -building_count are exactly those reachable from every building; take the min dist.
# 4. Early exit: If a building’s BFS can’t reach any eligible cell, return -1 immediately.

# Initialization:
#     dist[r][c]: total distance from all buildings to cell (r,c)
#     walk: starts at 0, used to mark eligible empty cells
#     buildings: counts total number of buildings
# BFS from Each Building:
#     For each building, perform BFS.
#     Only visit cells with value equal to walk.
#     Update dist[r][c] and mark visited cells by setting grid[r][c] = walk - 1.
# Final Scan:
#     After all BFS runs, scan the grid.
#     If grid[r][c] == -buildings, it means the cell was reached by all buildings.
#     Track the minimum distance among such cells.

# Time Complexity: O(m × n × b)
#     b = number of buildings
#     Each BFS traverses up to m × n cells
#     Optimized by skipping ineligible cells
# Space Complexity: O(m × n)
#     dist matrix
#     No extra visited matrix per BFS (uses grid in-place)

# No visited = [[False]*C for _ in range(R)] per building.
# Later BFS runs skip cells that some earlier building couldn’t reach.
# Same correctness, still O(B·R·C) worst-case, but much faster in
# practice with tighter memory use.

from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total_dist = [[0] * n for _ in range(m)]
        reach_count = [[0] * n for _ in range(m)]
        building_count = 0

        def bfs(start_x, start_y):
            visited = [[False] * n for _ in range(m)]
            q = deque([(start_x, start_y, 0)])
            visited[start_x][start_y] = True

            while q:
                x, y, dist = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        total_dist[nx][ny] += dist + 1
                        reach_count[nx][ny] += 1
                        q.append((nx, ny, dist + 1))

        # Step 1: BFS from each building
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building_count += 1
                    bfs(i, j)

        # Step 2: Find minimum distance where all buildings are reachable
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == building_count:
                    min_dist = min(min_dist, total_dist[i][j])

        return min_dist if min_dist != float('inf') else -1


def shortestDistance_optimized(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    R, C = len(grid), len(grid[0])
    dist = [[0]*C for _ in range(R)]

    buildings = 0
    walk = 0  # eligibility marker for empties

    def bfs(sr, sc) -> bool:
        nonlocal walk
        q = deque([(sr, sc, 0)])
        reached_any = False
        while q:
            r, c, d = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                # visit empty land only if still eligible for this round
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == walk:
                    grid[nr][nc] = walk - 1
                    dist[nr][nc] += d + 1
                    q.append((nr, nc, d + 1))
                    reached_any = True
        walk -= 1
        return reached_any

    # BFS from each building
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                buildings += 1
                if not bfs(r, c):
                    return -1  # this building can't reach any remaining eligible empty cell

    # Find best empty cell reached by all buildings
    ans = float('inf')
    for r in range(R):
        for c in range(C):
            if grid[r][c] == -buildings:  # reached by all
                ans = min(ans, dist[r][c])

    return ans if ans != float('inf') else -1