"""
763. Partition Labels
You are given a string s. We want to partition the string into as many parts as possible so that 
each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant 
string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
 
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

import collections
def partitionLabels(s: str):
    last = collections.defaultdict(int)
    end = 0
    for i in range(len(s)):        
        last[s[i]] = i
    i = 0
    size = 0
    res = []
    for i in range(len(s)):
        end = max(end, last[s[i]])
        size += 1
        if i == end:
            res.append(size)
            size = 0
    return res

# Test Cases
print(partitionLabels("ababcbacadefegdehijhklij")) # [9, 7, 8]
print(partitionLabels("caedbdedda")) # [1, 9]