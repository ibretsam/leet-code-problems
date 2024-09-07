"""
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[ ".Q..",
           "...Q",
           "Q...",
           "..Q."
          ],
          [
           "..Q.",
           "Q...",
           "...Q",
           ".Q.."
          ]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
 

Constraints:
1 <= n <= 9
"""
def solveNQueens(n):
    res = []

    def is_valid(row, col, board):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check top-left to bottom-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Check top-right to bottom-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == "Q":
                return False
        
        return True

    def backtrack(row, board):
        if row == n:
            res.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_valid(row, col, board):
                board[row][col] = "Q"
                backtrack(row + 1, board)
                board[row][col] = "."


    start = [["."] * n for _ in range(n)]
    backtrack(0, start)
    return res

# Test cases
print(solveNQueens(4)) # [[ ".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
print(solveNQueens(1)) # [["Q"]]