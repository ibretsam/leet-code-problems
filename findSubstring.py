"""
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are 
all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. 
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

def findSubstring(s, words):    
    res = []
    word_length = len(words[0])
    total_words_length = word_length * len(words)
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    for i in range(word_length):        
        l = i
        found_words = {}
        for r in range(i, len(s) - word_length + 1, word_length):                
            word = s[r : r + word_length]
            if word in words_count:
                found_words[word] = found_words.get(word, 0) + 1                
                while found_words[word] > words_count[word]:
                    found_words[s[l : l + word_length]] -= 1
                    l += word_length
                if r + word_length - l == total_words_length:                    
                    res.append(l)
            else:
                found_words = {}
                l = r + word_length          
    return res


print(findSubstring("barfoothefoobarman", ["foo","bar"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
print(findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
print(findSubstring("a", ["a"]))