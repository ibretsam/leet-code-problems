"""
79. Word Search
Medium
Topics
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

def exist(board, word):
        m, n = len(board), len(board[0])
        visited = set()

        def backtrack(curr_res, i, j):
            if len(curr_res) == len(word):
                if ''.join(curr_res) == word:
                    return True
                return False
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in direction:
                x, y = dx + i, dy + j
                if x in range(m) and y in range(n) and (x, y) not in visited and board[x][y] == word[len(curr_res)]:
                    curr_res.append(board[x][y])
                    visited.add((x, y))
                    if backtrack(curr_res, x, y):
                        return True
                    curr_res.pop()
                    visited.remove((x, y))
                
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if backtrack([board[i][j]], i, j):
                        return True
                    visited.remove((i, j))
        return False
                
# Test cases
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False