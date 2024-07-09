def orangesRotting(grid) -> int:
    n, m = len(grid), len(grid[0])
    rottens = []
    level = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 2:
                rottens.append([i, j, level])


    import collections
    q = collections.ChainMapdeque()
    for rotten in rottens:
        q.append(rotten)
    while q:
        x, y, lvl = q.popleft()
        level = lvl
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and grid[x][y] == 2:
                grid[nx][ny] = 2
                q.append([nx, ny, lvl + 1])
    
    for row in grid:
        for val in row:
            if val == 1:
                return -1
    return level

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1