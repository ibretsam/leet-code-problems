"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
"""

def convert(s, numRows):
    # Solution 1:
    res = [""] * numRows
    
    current_row, direction = 0, 1

    for c in s:
        res[current_row] += c
        if current_row == 0:
            direction = 1
        elif current_row == numRows - 1:
            direction = -1
        current_row += direction

    return ''.join(res)

    # Solution 2:
    # character_count = len(s)
    # while character_count > 0:
    #     for i in range(numRows):
    #         if character_count == 0:
    #             break
    #         res[i] += s[len(s) - character_count]
    #         character_count -= 1
    #     for i in range(numRows - 2, 0, -1):
    #         if character_count == 0:
    #             break
    #         res[i] += s[len(s) - character_count]
    #         character_count -= 1
        
    # return ''.join(res)

print(convert("PAYPALISHIRING", 3)) # "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4)) # "PINALSIGYAHRPI"
print(convert("PAYPALISHIRING", 5)) # "PHASIYIRPLIGAN"
print(convert("A", 1)) # "A"