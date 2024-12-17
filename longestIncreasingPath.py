"""
329. Longest Increasing Path in a Matrix
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally 
or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""
def longestIncreasingPath(matrix):
    """
    DFS with memoization
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    m, n = len(matrix), len(matrix[0])
    memo = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if memo[i][j] != -1:
            return memo[i][j]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        max_length = 1
        for dx, dy in directions:
            x, y = dx + i, dy + j
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                length = 1 + dfs(x, y)
                max_length = max(max_length, length)
        memo[i][j] = max_length
        return memo[i][j]
    max_path = 0
    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(i, j))

    return max_path

matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(longestIncreasingPath(matrix)) # 4

matrix = matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix)) # 4