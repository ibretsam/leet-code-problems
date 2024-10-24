"""
221. Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and 
return its area.

Example 1:
Input: matrix = 
[
	["1","0","1","0","0"],
	["1","0","1","1","1"],
	["1","1","1","1","1"],
	["1","0","0","1","0"]
]
Output: 4

Example 2:
Input: matrix = 
[
	["0","1"],
	["1","0"]
]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
def maximalSquare(matrix) -> int:
	m, n = len(matrix), len(matrix[0])
	dp = [[0] * n for _ in range(m)]
	for i in range(m - 1, -1, -1):
			for j in range(n - 1, -1, -1):
					if i == m - 1 or j == n - 1:
							dp[i][j] = int(matrix[i][j])
					else:
							if matrix[i][j] == "1":
									dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
							else:
									dp[i][j] = 0
	return max(max(row) for row in dp) ** 2

print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 4
