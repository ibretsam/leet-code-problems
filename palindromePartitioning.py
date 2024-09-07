"""
131. Palindrome Partitioning
Given a string s, partition s such that every  substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""
def partition(s):
    res = []

    def is_palindrome(s):
        return s == s[::-1]
    
    def backtrack(i, curr_res):
        if i == len(s):
            res.append(curr_res[:])
            return
        
        for c in range(i, len(s)):
            if is_palindrome(s[i : c + 1]):
                curr_res.append(s[i : c + 1])
                backtrack(c + 1, curr_res)
                curr_res.pop()

    backtrack(0, [])
    return res

# Test cases
print(partition("aab")) # [["a","a","b"],["aa","b"]]
print(partition("a")) # [["a"]]