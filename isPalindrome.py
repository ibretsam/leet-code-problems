def isPalindrome(s) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c
    return newStr
    
s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))
