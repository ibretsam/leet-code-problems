def canJump(nums):
    if len(nums) == 1:
        return True
    max_reach = 0
    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])
        if i >= max_reach:
            return False
        
    return True

print(canJump([2,3,1,1,4])) # True
print(canJump([3,2,1,0,4])) # False
print(canJump([0])) # True