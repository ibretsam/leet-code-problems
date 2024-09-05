"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
def generateParenthesis(n):
    res = []
    total_paren = n * 2
    def backtrack(open_count, close_count, curr_res):
        if len(curr_res) == total_paren:
            res.append(curr_res)
            return
        
        if open_count < n:
            backtrack(open_count + 1, close_count, curr_res + "(")

        if close_count < open_count:
            backtrack(open_count, close_count + 1, curr_res + ")")

    backtrack(0, 0, "")
    return res

# Test cases
print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1)) # ["()"]