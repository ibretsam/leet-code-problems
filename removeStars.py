def removeStars(s) -> str:
    s = list(s)
    while '*' in s:
        for i, c in enumerate(s):
            if c == '*':
                s.pop(i)
                s.pop(i - 1)
                break
    return ''.join(s)
    

print(removeStars("erase*****"))
