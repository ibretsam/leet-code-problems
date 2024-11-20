"""
416. Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such that 
the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

def canPartition(nums) -> bool:
    """
    Dynamic Programming (Top Down)
    - Time Complexity: O(n * sum(nums)) where n is the length of the nums array
    - Space Complexity: O(n * sum(nums))    
    """
    if sum(nums) % 2:
        return False

    memo = {}
    def dfs(i, target):
        if (i, target) in memo:
            return memo[(i, target)]
        if i >= len(nums):
            return target == 0
        if target < 0:
            return False

        memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
        return memo[(i, target)]

    return dfs(0, sum(nums) // 2)

def canPartition(nums):
    """
    Dynamic Programming (Bottom Up)
    - Time Complexity: O(n * sum(nums)) where n is the length of the nums array
    - Space Complexity: O(sum(nums))    
    """
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    dp = [False] * (target + 1)

    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

print(canPartition([2,2,1,1])) # True