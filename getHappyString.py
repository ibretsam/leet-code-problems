"""
1415. The k-th Lexicographical String of All Happy Strings of Length n

A happy string is a string that:

    consists only of letters of the set ['a', 'b', 'c'].
    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings 
"aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in 
lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy 
strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 
["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. 
You will find the 9th string = "cab"

Constraints:
    1 <= n <= 10
    1 <= k <= 100
"""
def getHappyString(n: int, k: int) -> str:
    """
    Time: O(3 * 2^(n-1)) - Generate all possible happy strings
    Space: O(3 * 2^(n-1)) - Store all possible happy strings    
    """
    happy = set()
    chars = ["a", "b", "c"]
    def gen_happy(curr_str):
        if len(curr_str) == n:
            happy.add(curr_str)
            return True
        for c in chars:                
            if curr_str and c == curr_str[-1]:
                continue
            curr_str += c
            if gen_happy(curr_str):
                curr_str = curr_str[:-1]
        return True
    gen_happy("")    
    return sorted(list(happy))[k - 1] if k <= len(happy) else ""


def getHappyString(n: int, k: int) -> str:
    """
    Time: O(min(k, 3 * 2^(n-1))) - Only generate up to k strings
    Space: O(n) - Recursion depth
    """
    # Calculate max possible strings: 3 * 2^(n-1)
    # First char: 3 choices, Others: 2 choices each
    max_strings = 3 * (2**(n - 1))
    if k > max_strings:
        return ""
        
    chars = ['a', 'b', 'c']
    count = [0]  # Use list to modify in closure
    result = [""]  # Store result when found
    
    def backtrack(curr):
        if len(curr) == n:
            count[0] += 1
            if count[0] == k:
                result[0] = curr
                return True
            return False
            
        for c in chars:
            if not curr or c != curr[-1]:
                if backtrack(curr + c):
                    return True
        return False
    
    backtrack("")
    return result[0]

# print(getHappyString(1, 3)) #"c"
# print(getHappyString(1, 4)) #"a"
print(getHappyString(3, 9)) #"cab"