"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
| 1 1 1 |       | 1 0 1 |
| 1 0 1 |   =>  | 0 0 0 |
| 1 1 1 |       | 1 0 1 |

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

| 0 1 2 0 |       | 0 0 0 0 |
| 3 4 5 2 |   =>  | 3 4 5 0 |
| 1 3 1 5 |       | 1 3 1 0 |

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""
def setZeroes(matrix):
    zero_positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_positions.append([i, j])

    for position in zero_positions:
        x, y = position
        for i in range(len(matrix[0])):
            matrix[x][i] = 0
        for j in range(len(matrix)):
            matrix[j][y] = 0

    return matrix
    
    

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))