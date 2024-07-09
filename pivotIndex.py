def pivotIndex(nums) -> int:
    sumLeft, sumRight = [], []
    currSumLeft, currSumRight = 0, 0
    for num in nums:
        currSumLeft += num
        sumLeft.append(currSumLeft)
    for num in nums[::-1]:
        currSumRight += num
        sumRight.append(currSumRight)
    print(sumLeft, sumRight)
    for i in range(len(sumLeft)):
        if sumLeft[i] == sumRight[i]:
            return i
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
# print([1,7,3,6,5,6][::-1])
for num in [1, 7, 3, 6, 5, 6][::-1]:
    print(num)
