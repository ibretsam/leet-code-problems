"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def countSubstrings(s) -> int:
    """
    Expand Around Center
    - Time Complexity: O(n^2) where n is the length of the string
    - Space Complexity: O(1)
    """
    res = 0
    def check(s, left, right):
        nonlocal res
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
    
    for i in range(len(s)):
        check(s, i, i)
        check(s, i, i + 1)
        
    return res

def countSubstrings(s) -> int:
    """
    Dynamic Programming
    - Time Complexity: O(n^2) where n is the length of the string
    - Space Complexity: O(n^2)
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = 0

    for i in range(n):
        dp[i][i] = True
        res += 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            res += 1

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                res += 1

    return res

print(countSubstrings("abc")) # 3
print(countSubstrings("aaa")) # 6
print(countSubstrings("aaabbbccc")) # 18