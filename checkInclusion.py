"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""
from collections import Counter, defaultdict

def checkInclusion(s1, s2) -> bool:
    freq = Counter(s1)
    l = 0
    curr_map = defaultdict(int)
    for r in range(len(s2)):
        curr_map[s2[r]] += 1
        if r - l + 1 > len(s1):
            if curr_map[s2[l]] == 1:
                del curr_map[s2[l]]
            else:
                curr_map[s2[l]] -= 1
            l += 1
        if curr_map == freq:
            return True
    return False

# Test cases
print(checkInclusion("ab", "eidbaooo"))  # True
print(checkInclusion("ab", "eidboaoo"))  # False
print(checkInclusion("hello", "ooolleoooleh")) # Expected False