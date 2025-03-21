"""
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to 
bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    
    return dp[-1]


# Test cases
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid)) # 7
grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid)) # 12