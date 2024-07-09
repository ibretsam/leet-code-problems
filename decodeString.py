import re
def decodeString(s):
    stk = []
    for c in s:
        if c != "]":
            stk.append(c)
        else:
            curr = ""
            while stk and stk[-1] != "[":
                curr = stk.pop() + curr
            stk.pop()
            currNum = ""
            while stk and stk[-1].isdigit():
                currNum = stk.pop() + currNum
            stk.append(int(currNum) * curr)
    return ''.join(stk)

# print(decodeString("3[a]2[bc]")) # "aaabcbc"
# print(decodeString("3[a2[c]]")) # "accaccacc"
# print(decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"
print(decodeString("100[leetcode]"))
print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
