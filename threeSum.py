"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def threeSum(nums):
    def twoSum(numbers, target):
        l, r, res = 0, len(numbers) - 1, []
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.append([l + 1, r + 1])
                l += 1
                r -= 1
                while l < r and numbers[l] == numbers[l - 1]:
                    l += 1
                while l < r and numbers[r] == numbers[r + 1]:
                    r -= 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return res
    
    nums.sort()
    res = []
    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        datas = twoSum(nums[i + 1:], -num)  
        if datas != []:
            for data in datas:
                curr_res = [num, nums[data[0] + i], nums[data[1] + i]]
                res.append(curr_res)             
    return res

    
nums = [-2,0,0,2,2]
print(threeSum(nums))