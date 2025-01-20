"""
2661. First Completely Painted Row or Column

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. 
arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the 
integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

Example 1:
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

Example 2:
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].

Constraints:
    m == mat.length
    n = mat[i].length
    arr.length == m * n
    1 <= m, n <= 10^5
    1 <= m * n <= 10^5
    1 <= arr[i], mat[r][c] <= m * n
    All the integers of arr are unique.
    All the integers of mat are unique.
"""
def firstCompleteIndex(arr, mat) -> int:
    """
    The idea is to keep track of the number of times a row or column has been painted.
    We can do this by keeping track of the count of each row and column.
    Time Complexity: O(m*n)
    Space Complexity: O(m+n)
    """
    m, n = len(mat), len(mat[0])
    pos = {}
    for i in range(m):
        for j in range(n):
            pos[mat[i][j]] = (i, j)
    row_count = [0] * m
    col_count = [0] * n

    for index, num in enumerate(arr):
        i, j = pos[num]
        row_count[i] += 1
        col_count[j] += 1

        if row_count[i] == n or col_count[j] == m:
            return index

print(firstCompleteIndex([1,3,4,2], [[1,4],[2,3]])) # 2
print(firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]])) # 3