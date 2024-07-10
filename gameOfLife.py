"""
289. Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton 
devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) 
or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the 
next state.

Example 1:

| 0 | 1 | 0 |       | 0 | 0 | 0 |
| 0 | 0 | 1 |  =>   | 1 | 0 | 1 |
| 1 | 1 | 1 |       | 0 | 1 | 1 |
| 0 | 0 | 0 |       | 0 | 1 | 0 |
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

| 1 | 1 |       | 1 | 1 |
| 1 | 0 |  =>   | 1 | 1 |
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update 
some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would 
cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). 
How would you address these problems?
"""
def gameOfLife(board):
    m = len(board[0])
    n = len(board)
    board_2 = [row[:] for row in board]
    for i in range(n):
        for j in range(m):
            neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i,  j + 1), (i + 1,j - 1), (i + 1, j), (i + 1, j + 1)]
            count_lives, count_deaths = 0, 0
            for neighbor in neighbors:
                x, y = neighbor
                if x >= 0 and x < n and y >= 0 and y < m:
                    if board_2[x][y] == 0:
                        count_deaths += 1
                    elif board_2[x][y] == 1:
                        count_lives += 1
            if board_2[i][j] == 1:
                if count_lives < 2 or count_lives > 3:
                    board[i][j] = 0
            elif board_2[i][j] == 0:
                if count_lives == 3:
                    board[i][j] = 1
    return board

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))