"""
322. Coin Change
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount 
of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

def coinChange(coins, amount):
    # Top-down approach
    # if amount == 0:
    #     return amount
    # def dp(amount, coins, memo):
    #     fewest_combination = None
    #     if amount in memo:
    #         return memo[amount]
    #     if amount == 0:
    #         return []
    #     if amount < 0:
    #         return None
        
    #     for coin in coins:
    #         curr_comb = dp(amount - coin, coins, memo)
    #         if curr_comb != None:
    #             combination = curr_comb + [coin]
    #             if not fewest_combination or len(combination) < len(fewest_combination):
    #                 fewest_combination = combination
    #                 memo[amount] = fewest_combination
    #     memo[amount] = fewest_combination
    #     return memo[amount]
    # res = dp(amount, coins, {})
    # return len(res) if res else -1

    # Bottom-up approach
    if amount == 0:
        return amount
    dp = [None] * (amount + 1)
    dp[0] = []
    for i in range(amount + 1):
        if dp[i] is not None:
            for coin in coins:            
                if i + coin <= amount:
                    combination = dp[i] + [coin]
                    if dp[i + coin] is None or len(combination) < len(dp[i + coin]):
                        dp[i + coin] = combination
    res = dp[-1]
    return len(res) if res else -1

# Test cases
print(coinChange([1,2,5], 11)) # Expected output: 3
print(coinChange([2], 3)) # Expected output: -1
print(coinChange([1], 0)) # Expected output: 0
print(coinChange([1], 1)) # Expected output: 1