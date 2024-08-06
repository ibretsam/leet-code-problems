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
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

def calculate(s):
    stack = []
    operators = ["+", "-"]
    curr_operators = []
    for i, c in enumerate(s):
        if c.isnumeric():
            stack.append(int(c))
            if curr_operators:
                operator = curr_operators.pop()
                num1, num2 = stack.pop(), stack.pop()
                if operator == "+":
                    stack.append(num1 + num2)
                else:
                    stack.append(num2 - num1)
        elif c in operators:
            curr_operators.append(c)
    s = [str(i) for i in stack]
    return int("".join(s))


# print(calculate("1 + 1")) # 2
# print(calculate(" 2-1 + 2 ")) # 3
# print(calculate("(1+(4+5+2)-3)+(6+8)")) # 23
# print(calculate("2147483647")) # 2147483647
print(calculate("1-(     -2)")) # 3