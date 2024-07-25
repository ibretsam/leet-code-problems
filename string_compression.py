"""
443. String Compression
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 
Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

def compress(chars):
#     i = j = 0
#     while i < len(chars):
#         char = chars[i]
#         count = 0
#         while i < len(chars) and chars[i] == char:
#             i += 1
#             count += 1
#         chars[j] = char
#         j += 1
#         if count > 1:
#             for digit in str(count):
#                 chars[j] = digit
#                 j += 1
#     return chars[:j]

    for i, c in enumerate(chars):
        count = 0
        if i != len(chars) - 1 and chars[i + 1] == c:
            count += 1
            j = i + 1
            while j <= len(chars) - 1 and chars[j] == c:
                count += 1
                chars.pop(j)
            if count < 9:
                chars.insert(i + 1, str(count))
            else:
                print(count)
                for k, ch in enumerate(str(count)):
                    chars.insert(i + k + 1, ch)
    return chars
    
print(compress(["a","a","b","b","c","c","c","c"]))
print(compress(["a", "a", "2", "2", "2"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(compress(["b","l","l","l","l","l","l","4","4","W","W","&","d","d","d","@","D","D",".",".",".","8","8","8","U","V",">","J","J","k","H","H","=","l","[","[","[","[","[","[","[","a","a","'","<","[","[","y","V","l","l","'","$","E","`","v","k","E","E","t","t","t","t","t","=","=","0","C","a","l","l","l","r","R","M","M","c","c","c","A","A","S","9","9","9","9",")",")","\\","s","\\","\\","y","W","W","W","J","J","J","J","6","6","<","<","E","u","e","e","e","e","e","e","e","e","e","9","9","9","9","R","8","?","F","3","&","&","&","&","f","%","%","2","2","2",")",")",")","J","p","|","D","D","D","s","t","V","V","?","^","^","S","3","3","3","3","h","*","|","|","b","b","a","a","a","r","r","r","r","J",".","^","^","~","g",":",":",":","(","4","4","4","4","w","w","w","w","w","w","w","C","?","=","d","L",":","0","0","c","w","w","w","w","w","w","{","{","t","k","k","k","&","&","&","h","j","j","j","0","3","l",";",";",";",";",";",".",".",".","%","1","1","1","l","9","?","?","?","t",">","E","N","N","@",">",".",".","I","a","a","a","a","B","7","7","{","o","o","-","+","+","+","+","o","o","}","B","B","r","r","r","q","4","4","4","9","W","W","W","W","W","'","'","'","g","J","(","(","(","(","t","t","?",";","g","g","g","0","]","]","]"]))
    