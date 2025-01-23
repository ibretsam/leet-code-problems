"""
1267. Count Servers that Communicate
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that 
cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on 
the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server. 

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
def countServers(grid) -> int:
    m, n = len(grid), len(grid[0])
    row_count, col_count = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                res += 1
    return res

from collections import deque
def countServers(grid) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()

    def bfs(i, j):
        q = deque([(i, j)])
        count = 0
    
        while q:
            i, j = q.popleft()
            if (i, j) in visited:
                continue

            visited.add((i, j))
            count += 1

            for y in range(n):
                if y != j and grid[i][y] == 1 and (i, y) not in visited:
                    q.append((i, y))
            for x in range(m):
                if x != i and grid[x][j] == 1 and (x, j) not in visited:
                    q.append((x, j))
        return count if count > 1 else 0
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visited:
                res += bfs(i, j)
    return res

print(countServers([[1,0],[0,1]])) # 0
print(countServers([[1,0],[1,1]])) # 3
print(countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])) # 4