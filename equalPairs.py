def equalPairs(grid) -> int:
    print(grid)
    cols = []
    i = 0
    while i < len(grid):
        j = 0
        col = []
        while j < len(grid[i]):
            col.append(grid[j][i])
            j += 1
        cols.append(col)
        i += 1
    repr_cols = []
    for col in cols:
        repr_cols.append(str(col))
    print(repr_cols)
    count1, count2 = 0, 0
    for arr in grid:
        if arr in cols:
            count1 += 1
    for arr in cols:
        if arr in grid:
            count2 += 1
            
    return(max(count1, count2))

print(equalPairs([[3, 1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # 3
print(equalPairs([[13, 13], [13, 13]])) # 4
