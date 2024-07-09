def maxOperations(nums, k):
    if len(nums) == 1:
        return 0
    count = 0
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == k:
            count += 1
            l += 1
            r -= 1
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1
    return count
# print(maxOperations([1, 2, 3, 4], 5))  # 2
# print(maxOperations([3, 1, 3, 4, 3], 6))  # 1
# print(maxOperations([5,1,3,4,4], 6))  # 1
print(maxOperations([2,2,2,3,1,1,4,1], 4)) # 2