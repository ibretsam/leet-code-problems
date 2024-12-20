"""
312. Burst Balloons
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number 
on it represented by an array nums. You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon 
with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10
 
Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""
from functools import cache
def maxCoins(nums) -> int:
    """
    Brute Force with cache
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    nums = [1] + nums + [1]
    @cache
    def burst(l, r):
        if l > r:
            return 0
        max_coins = 0
        for i in range(l, r + 1):
            total = nums[l - 1] * nums[i] * nums[r + 1]
            total += burst(l, i - 1) + burst(i + 1, r)
            max_coins = max(max_coins, total)
        return max_coins
    return burst(1, len(nums) - 2)

def maxCoins(nums) -> int:
    """
    Bottom Up DP
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    n = len(nums)
    new_nums = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for l in range(n, 0, -1):
        for r in range(l, n + 1):
            for i in range(l, r + 1):
                coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                coins += dp[l][i - 1] + dp[i + 1][r]
                dp[l][r] = max(dp[l][r], coins)
    return dp[1][n]

nums = [3, 1, 5, 8]
print(maxCoins(nums)) # 167

nums = [1, 5]
print(maxCoins(nums)) # 10