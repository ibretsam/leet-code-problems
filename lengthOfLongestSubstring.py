"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    # O(n^2) because of the in operator
    # if len(s) == 0:
    #     return 0
    # max_length = 0
    # l, r = 0, 1
    # curr_length = 1
    # while r < len(s):
    #     if s[r] not in s[l : r]:
    #         curr_length = len(s[l : r + 1])
    #     else:
    #         max_length = max(max_length, curr_length)            
    #         while s[r] in s[l : r]:
    #             l += 1
    #             curr_length = len(s[l : r])
    #     r += 1
    # max_length = max(max_length, curr_length)
    # return max_length

    # O(n) using a hashmap
    max_length = 0
    l = 0
    char_index_map = {}
    for r in range(len(s)):
        if s[r] in char_index_map and char_index_map[s[r]] >= l:
            l = char_index_map[s[r]] + 1
        char_index_map[s[r]] = r
        max_length = max(max_length, r - l + 1)
    return max_length


# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("aab"))