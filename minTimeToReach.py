"""
3341. Find Minimum Time to Reach Last Room I
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start 
moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms 
takes exactly one second.
Return the minimum time to reach the room (n - 1, m - 1).
Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.

Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 3

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 10^9
"""
import heapq
def minTimeToReach(moveTime) -> int:
    m, n = len(moveTime), len(moveTime[0])
    min_heap = [(0, 0, 0)]
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while min_heap:
        t, r, c = heapq.heappop(min_heap)
        if (r, c) in visited:
            continue

        visited.add((r, c))
        if r == m - 1 and c == n - 1:
            return t
        
        for dx, dy in directions:
            x, y = dx + r, dy + c
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                heapq.heappush(min_heap, (max(t, moveTime[x][y]) + 1, x, y))
    return -1

print(minTimeToReach([[0,4],[4,4]]))