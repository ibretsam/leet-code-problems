"""
151. Reverse Words in a String
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated 
by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

def reverseWords(s: str) -> str:
    s = list(s)

    def reverse(l, start, end):
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1

    n = len(s)
    start = 0
    while start < n and s[start] == " ":
        start += 1
    
    end = n - 1
    while end >= 0 and s[end] == " ":
        end -= 1
    
    slow = 0
    while start <= end:
        if s[start] != " " or (slow > 0 and s[slow - 1] != " "):
            s[slow] = s[start]
            slow += 1
        start += 1
    reverse(s, 0, slow - 1)

    start = 0
    for end in range(slow):
        if s[end] == " ":
            reverse(s, start, end - 1)
            start = end + 1
    reverse(s, start, slow - 1)

    return "".join(s[:slow])


# print(reverseWords("the sky is blue")) # "blue is sky the"
print(reverseWords("  hello world  ")) # "world hello"
print(reverseWords("a good   example")) # "example good a"