"""
1639. Number of Ways to Form a Target String Given a Dictionary

You are given a list of strings of the same length words and a string target.
Your task is to form target using the given words under the following rules:
target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if 
target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string 
in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every 
string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.
Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:
Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 
Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
"""

from collections import defaultdict
def numWays(words, target):
    mod = 10 ** 9 + 7
    count = defaultdict(int)
    for word in words:
        for i, char in enumerate(word):
            count[(i, char)] += 1
    cache = {}
    m, n = len(target), len(words[0])
    def dfs(i, k):
        if i == m:
            return 1
        if k == n:
            return 0
        if (i, k) in cache:
            return cache[(i, k)]
        char = target[i]
        cache[(i, k)] = dfs(i, k + 1)
        if count[(k, char)] == 0:
            return cache[(i, k)] % mod
        cache[(i, k)] += count[(k, char)] * dfs(i + 1, k + 1)
        return cache[(i, k)] % mod
    return dfs(0, 0)

def numWays(words, target):
    mod = 10 ** 9 + 7
    m, n  = len(target), len(words[0])

    # Count occurrences of each character in each column
    col_counts = [{} for _ in range(n)]
    for word in words:
        for i, char in enumerate(word):
            col_counts[i][char] = col_counts[i].get(char, 0) + 1
    
    dp = [0] * (m + 1)
    dp[0] = 1

    for j in range(n):
        for i in range(m, 0, -1):
            dp[i] += dp[i - 1] * col_counts[j].get(target[i - 1], 0)
            dp[i] %= mod
    return dp[m]
words = ["acca","bbbb","caca"]
target = "aba"
print(numWays(words, target))