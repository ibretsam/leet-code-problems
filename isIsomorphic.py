"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order 
of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 
Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

def canConstruct(s, t):
    if len(s) != len(t):
        return False
    s_dict, t_dict = {}, {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = t[i]
        if t[i] not in t_dict:
            t_dict[t[i]] = s[i]
        if s_dict[s[i]] != t[i] or t_dict[t[i]] != s[i]:
            return False
    return True        

print(canConstruct("bbbaaaba", "aaabbbba"))
print(canConstruct("foo", "bar"))
print(canConstruct("paper", "title"))