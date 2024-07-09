"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
 _ _ _ _ _ _
| 1 → 2 → 3 |
|         ↓ |
| 4 → 5   6 |
| ↑       ↓ |
| 7 ← 8 ← 9 |
 ‾ ‾ ‾ ‾ ‾ ‾
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
 __ _ _ _ _ _ _ _ _ 
| 1  → 2  → 3  → 4 |
|                ↓ |
| 5  → 6  → 7    8 |
| ↑              ↓ |
| 9 ← 10 ← 11 ← 12 |
 ‾‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

def spiralOrder(matrix):
    if len(matrix) == 1:
        return matrix[0]

    res = []
    first_row = 0
    last_column = len(matrix[0]) 
    last_row = len(matrix)
    first_column = 0
    while first_row < last_row and first_column < last_column:
        for i in range(first_column, last_column):
            res.append(matrix[first_row][i])
        first_row += 1

        for j in range(first_row, last_row):
            res.append(matrix[j][last_column - 1])
        last_column -= 1

        if not (first_row < last_row and first_column < last_column):
            break 
        
        for k in range(last_column - 1, first_column - 1, -1):                
            res.append(matrix[last_row - 1][k])
        last_row -= 1

        
        for l in range(last_row - 1, first_row - 1, -1):        
            res.append(matrix[l][first_column])
        first_column += 1

    return res

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiralOrder([[7],[9],[6]]))
print(spiralOrder([[2,5,8],[4,0,-1]]))