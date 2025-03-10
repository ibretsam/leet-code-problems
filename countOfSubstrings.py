"""
3306. Count of Substrings Containing Every Vowel and K Consonants II
You are given a string word and a non-negative integer k.
Return the total number of
of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:

    word[0..5], which is "ieaouq".
    word[6..11], which is "qieaou".
    word[7..12], which is "ieaouq".

Constraints:
    5 <= word.length <= 2 * 10^5
    word consists only of lowercase English letters.
    0 <= k <= word.length - 5
"""
from collections import defaultdict
def countOfSubstrings(word: str, k: int) -> int:
    def atleast_k(k):
        vowels = "aieou"
        vowels_map = defaultdict(int)
        left, res, cons_count = 0, 0, 0
        for right in range(len(word)):
            if word[right] in vowels:
                vowels_map[word[right]] += 1
            else:
                cons_count += 1

            while len(vowels_map) == 5 and cons_count >= k:
                res += len(word) - right
                if word[left] in vowels:
                    vowels_map[word[left]] -= 1
                else:
                    cons_count -= 1
                
                if vowels_map[word[left]] == 0:
                    vowels_map.pop(word[left])
                left += 1
        return res

    return atleast_k(k) - atleast_k(k + 1)

print(countOfSubstrings("ieaouqqieaouqq", 1)) # 3
print(countOfSubstrings("aeiou", 0)) # 1
print(countOfSubstrings("aeioqq", 1)) # 0
print(countOfSubstrings("iqeaouqi", 2)) # 3
print(countOfSubstrings("buoeia", 0)) # 1