"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

def minSubArrayLen(target, nums):
    l = 0
    res = float('inf')
    currSum = 0
    for r in range(len(nums)):
        currSum += nums[r]
        while currSum >= target:
            res = min(res, r - l + 1)
            currSum -= nums[l]
            l += 1        
    return res if res != float('inf') else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(minSubArrayLen(11, [1,2,3,4,5]))
print(minSubArrayLen(80, [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))
print(minSubArrayLen(10, [10,2,3]))