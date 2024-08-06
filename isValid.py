"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    stack = []
    pair_map = {
        '(':')',
        '{':'}',
        '[':']'
    }
    for c in s:
        if c in pair_map:
            stack.append(c)
        elif c in pair_map.values():
            if not stack or c != pair_map[stack[-1]]:
                return False            
            stack.pop()
    return True if not stack else False

print(isValid("(("))
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("){"))
print(isValid("{[]}"))