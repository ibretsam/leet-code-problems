"""

125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

def isPalindrome(s) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()    
    return newStr == newStr[::-1]
    
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
