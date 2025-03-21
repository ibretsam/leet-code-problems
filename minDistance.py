"""
72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert 
word1 to word2.

You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""
# Bottom-up approach
def minDistance(word1: str, word2: str) -> int:
    dp = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word2) + 1):
        dp[len(word1)][i] = len(word2) - i
    for j in range(len(word1) + 1):
        dp[j][len(word2)] = len(word1) - j

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
    
    return dp[0][0]

# Top-down approach
from functools import cache
def minDistance(word1: str, word2: str) -> int:
    @cache
    def dfs(i, j):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)
        else:
            return 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
    return dfs(0, 0)

# Test cases:
print(minDistance("horse", "ros")) # Output: 3
print(minDistance("intention", "execution")) # Output: 5