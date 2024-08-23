"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
def numIslands(grid):
    m = len(grid)
    n = len(grid[0])

    visited = set()
    num_islands = 0

    def dfs(r, c):
        stack = []
        visited.add((r, c))
        stack.append((r, c))
        while stack:
            row, col = stack.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                x, y = row + dx, col + dy
                if (x in range(m) and y in range(n)):
                    if (grid[x][y] == "1") and (x, y) not in visited:
                        stack.append((x, y))
                        visited.add((x, y))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and (i, j) not in visited:
                dfs(i, j)
                num_islands += 1

    return num_islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))