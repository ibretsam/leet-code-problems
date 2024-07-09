"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
"""

def isSubsequence(s: str, t: str) -> bool:
    if s == t:
        return True
    if len(t) <= 1:
        return False
    l, r = 0, 0
    longer = s if len(s) > len(t) else t
    shorter = t if len(s) > len(t) else s
    while r < len(longer):
        if l < len(shorter) and shorter[l] == longer[r]:
            l += 1
            r += 1
        else:
            r += 1
    return True if l == len(shorter) else False

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("aa", "a"))
print(isSubsequence("", "ahbgdc")) # True
print(isSubsequence("abc", "")) # False