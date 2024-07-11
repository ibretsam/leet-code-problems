"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
| 1 | 2 | 3 |       | 7 | 4 | 1 |
| 4 | 5 | 6 |  =>   | 8 | 5 | 2 |
| 7 | 8 | 9 |       | 9 | 6 | 3 |

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
| 05 | 01 | 09 | 11 |       | 15 | 13 | 02 | 05 |
| 02 | 04 | 08 | 10 |  =>   | 14 | 03 | 04 | 01 |
| 13 | 03 | 06 | 07 |       | 12 | 06 | 08 | 09 |
| 15 | 14 | 12 | 16 |       | 16 | 07 | 10 | 11 |

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
def rotate(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix

    # Another approach:
    # m = len(matrix)
    # for i in range(m // 2):
    #     for j in range(i, m - i - 1):
    #         matrix[i][j], matrix[m - 1 - j][i], matrix[m - 1 - i][m - 1 - j], matrix[j][m - 1 - i] = matrix[m - 1 - j][i], matrix[m - 1 - i][m - 1 - j], matrix[j][m - 1 - i], matrix[i][j]  
print(rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
# print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# print(rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])) # [[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]]...
# print(rotate([[24,4,38,2,21,18,33,40],[24,37,25,62,37,15,35,36],[42,23,13,58,17,26,19,8],[32,48,9,58,36,18,40,61],[23,16,0,46,35,34,23,60],[9,49,60,47,1,32,20,45],[56,34,40,11,61,60,20,30],[45,30,25,18,49,3,16,10]]))