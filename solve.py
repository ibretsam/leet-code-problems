"""
130. Surrounded Regions
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region 
cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

def solve(board):
    m, n = len(board), len(board[0])

    def dfs(i, j):
        stack = [(i, j)]

        while stack:
            r, c = stack.pop()
            if board[r][c] == "O":
                board[r][c] = "T"
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                x, y = dx + r, dy + c
                if x in range(m) and y in range(n):
                    if board[x][y] == "O" and (x, y):
                        stack.append((x, y))


    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O":
                dfs(i, j)
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == "T":
                board[i][j] = "O"

    return board


# Test cases
print(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
print(solve([["X"]])) # [["X"]]