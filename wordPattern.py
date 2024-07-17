"""
290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
def wordPattern(pattern, s):
    s = s.split()
    if len(pattern) != len(s):
        return False
    pattern_dict, s_dict = {}, {}
    for i in range(len(s)):
        if pattern[i] not in pattern_dict:
            pattern_dict[pattern[i]] = s[i]
        if s[i] not in s_dict:
            s_dict[s[i]] = pattern[i]
        if pattern_dict[pattern[i]] != s[i] or s_dict[s[i]] != pattern[i]:
            return False

    return True

print(wordPattern("abba", "dog cat cat dog")) # True
print(wordPattern("abba", "dog cat cat fish")) # False
print(wordPattern("aaaa", "dog cat cat dog")) # False