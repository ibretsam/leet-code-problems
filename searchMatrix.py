def searchMatrix(matrix, target) -> bool:
    if not matrix or not matrix[0]:
            return False
            
    lrow, rrow = 0, len(matrix) - 1
    while lrow <= rrow:
        mrow = (lrow + rrow) // 2
        if matrix[mrow][0] > target:
            rrow = mrow - 1
        elif matrix[mrow][-1] < target:
            lrow = mrow + 1
        else:
            l, r = 0, len(matrix[mrow]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[mrow][mid] > target: 
                    r = mid - 1
                elif matrix[mrow][mid] < target:
                    l = mid + 1
                else:
                    return True
    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))