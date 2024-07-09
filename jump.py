def jump(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 1
    jumps = 0
    max_reach = steps = nums[0]
    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            return jumps + 1
        max_reach = max(max_reach, i + nums[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps
        

# print(jump([2,3,1,1,4])) # 2
# print(jump([2,3,0,1,4])) # 2
# print(jump([2,1]))
# print(jump([1,3,2]))
print(jump([1,2,1,1,1]))