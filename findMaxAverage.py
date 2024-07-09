def findMaxAverage(nums, k):
    if len(nums) == 1:
        return nums[0]
    avgList = []
    l, r = 0, k
    currSum = sum(nums[:k])
    avgList.append(currSum/k)
    while r < len(nums):
        l += 1
        r += 1
        currSum = currSum - nums[l - 1] + nums[r - 1]
        avgList.append(round(currSum/k, 5))

    return max(avgList)

print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(findMaxAverage([5], 1))  # 5.0
print(findMaxAverage([0, 1,1,3,3], 4))  # 2.00000