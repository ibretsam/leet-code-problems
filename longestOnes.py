def longestOnes(nums, k):
    if k == 0  and 0 not in nums:
        return len(nums)
    if k == 0 and 1 not in nums:
        return 0
    currMax = 0
    l, r = 0, 0
    tempK = k
    while r < len(nums):
        if nums[r] == 0:
            tempK -= 1
        if tempK < 0:
            tempK = 0
        if tempK == 0:
            if len(nums[l: r]) > currMax:
                currMax = len(nums[l: r])
            if r < len(nums) - 1 and nums[r + 1] == 0:                   
                l += 1
                r = l
                tempK = k
            # else:
            #     l = r + 1
            #     r = l
            #     tempK = k
        if r == len(nums) - 1:
            if nums[r] == 1:
                if len(nums[l : r + 1]) > currMax:
                    currMax = len(nums[l : r + 1])
        r += 1
    return currMax

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)) # 10
print(longestOnes([0,0,1,1,1,0,0], 0)) # 3
print(longestOnes([0,0,0,0], 0)) # 0
print(longestOnes([0,0,0,1], 4)) # 4
print(longestOnes([1, 1,1,0,0,0,1,1,1,1], 0)) # 4