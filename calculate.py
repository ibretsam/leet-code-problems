"""
224. Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:
1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

def calculate(s):
    sign, sum, stack = 1, 0, []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = []
            while i < len(s) and s[i].isdigit():
                num.append(s[i])
                i += 1
            sum += int(''.join(num)) * sign
            i -= 1
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack.append(sum)
            stack.append(sign)
            sum = 0
            sign = 1
        elif s[i] == ')':
            sum = stack.pop() * sum
            sum += stack.pop()
        i += 1
    return sum

print(calculate("1 + 1")) # 2
print(calculate(" 2-1 + 2 ")) # 3
print(calculate("(1+(4+5+2)-3)+(6+8)")) # 23
print(calculate("2147483647")) # 2147483647
print(calculate("1-(     -2)")) # 3
print(calculate("2147483647"))