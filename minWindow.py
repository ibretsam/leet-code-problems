"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in 
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter

def minWindow(s: str, t: str) -> str:
    char_count = Counter(t)
    curr_str = Counter()
    
    l = 0
    min_length = float("inf")
    min_start = 0  # To remember the start of the minimum window
    
    required = len(char_count)  # Number of unique characters in t that need to be present in the window
    formed = 0  # Number of unique characters in t that are currently right in the window
    
    for r in range(len(s)):
        c = s[r]
        curr_str[c] += 1
        
        if c in char_count and curr_str[c] == char_count[c]:
            formed += 1
        
        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            c = s[l]
            
            # Save the smallest window until now.
            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_start = l
            
            curr_str[c] -= 1
            if c in char_count and curr_str[c] < char_count[c]:
                formed -= 1
            
            l += 1
    
    return "" if min_length == float("inf") else s[min_start:min_start + min_length]


print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(minWindow("aa", "aa")) # "aa"
print(minWindow("a", "aa")) # ""
print(minWindow("bba", "ab")) # ba