"""
407. Trapping Rain Water II
Given an m x n integer matrix heightMap representing the height of each unit cell in 
a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:
    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 10^4
"""
import heapq
def trapRainWater(heightMap) -> int:
    m, n = len(heightMap), len(heightMap[0])
    visited = set()
    heap = []
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited.add((i, j))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_height = 0
    volume = 0

    while heap:
        height, i, j = heapq.heappop(heap)
        max_height = max(max_height, height)

        for dx, dy in directions:
            x, y = dx + i, dy + j
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                visited.add((x, y))
                if heightMap[x][y] < max_height:
                    volume += max_height - heightMap[x][y]
                heapq.heappush(heap, (heightMap[x][y], x, y))

    return volume

print(trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])) # 4
print(trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])) # 14