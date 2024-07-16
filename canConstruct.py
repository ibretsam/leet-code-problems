"""
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
import collections
def canConstruct(ransomNote, magazine):
    freq_mag = collections.Counter(magazine)
    freq_ran = collections.Counter(ransomNote)

    for c in ransomNote:
        if c in freq_ran and c not in freq_mag:
             return False
             
        if freq_mag[c] < freq_ran[c]:
                return False        

    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
print(canConstruct("abcd", "dcba"))