"""
778. Swim in Rising Water
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally 
adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in 
zero time. Of course, you must stay within the boundaries of the grid during your swim.
Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 
Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n^2
Each value grid[i][j] is unique.
"""
import heapq
def swimInWater(grid) -> int:
    """
    Using Djikstra's Algorithm
    Time Complexity: O(n^2log(n))
    Space Complexity: O(n^2)
    """
    n = len(grid)
    visited = set()
    min_heap = [[grid[0][0], 0, 0]]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while min_heap:
        curr_max, i, j = heapq.heappop(min_heap)
        if i == j == n - 1:
            return curr_max
        if (i, j) not in visited:
            visited.add((i, j))
            for dx, dy in directions:
                x, y = dx + i, dy + j
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    new_max = max(curr_max, grid[x][y])
                    heapq.heappush(min_heap, [new_max, x, y])

grid = [[0,2],[1,3]]
print(swimInWater(grid)) # 3