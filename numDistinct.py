"""
115. Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
r̳a̳b̳b̳bi̳t̳
r̳a̳bb̳b̳i̳t̳
r̳a̳b̳bb̳i̳t̳

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
b̳a̳bg̳bag
b̳a̳bgbag̳
b̳abgba̳g̳
bab̳gba̳g̳
babgb̳a̳g̳
 
Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""
from functools import cache
def numDistinct(s: str, t: str) -> int:
    """
    Brute Force using cache
    Time Complexity: O(2^N) where N is length of s
    Space Complexity: O(N)
    """
    @cache
    def dp(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        
        res = dp(i + 1, j)
        if s[i] == t[j]:
            res += dp(i + 1, j + 1)
        return res
    return dp(0, 0)

def numDistinct(s: str, t: str) -> int:
    """
    Top Down DP with memoization
    Time Complexity: O(N * M) where N is length of s and M is length of t
    Space Complexity: O(N * M)    
    """
    cache = {}
    def dp(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        
        res = dp(i + 1, j)
        if s[i] == t[j]:
            res += dp(i + 1, j + 1)
        cache[(i, j)] = res
        return res
    return dp(0, 0)

def numDistinct(s: str, t: str) -> int:
    """
    Bottom Up DP
    Time Complexity: O(N * M) where N is length of s and M is length of t
    Space Complexity: O(N * M)
    """
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = dp[i + 1][j]
            if s[i] == t[j]:
                dp[i][j] += dp[i + 1][j + 1]
    return dp[0][0]

def numDistinct(s: str, t: str) -> int:
    """
    Bottom Up DP with Space Optimization
    Time Complexity: O(N * M) where N is length of s and M is length of t
    Space Complexity: O(M)    
    """
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    next_dp = [0] * (n + 1)

    dp[n] = next_dp[n] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            next_dp[j] = dp[j]
            if s[i] == t[j]:
                next_dp[j] += dp[j + 1]
        dp = next_dp[:]
    return next_dp[0]

print(numDistinct("rabbbit", "rabbit")) # 3