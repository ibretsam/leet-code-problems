"""
2094. Finding 3-Digit Even Numbers
You are given an integer array digits, where each element is a digit. 
The array may contain duplicates.
You need to find all the unique integers that follow the given requirements:
The integer consists of the concatenation of three elements from digits in any 
arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
Return a sorted array of the unique integers.

Example 1:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.

Example 2:
Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 

Example 3:
Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.

Constraints:
3 <= digits.length <= 100
0 <= digits[i] <= 9
"""

from collections import Counter, defaultdict
def findEvenNumbers(digits):
    """
    Find each valid digit
    """
    # More efficient solution
    result = set()  # Use set to automatically handle duplicates
    count = Counter(digits)
    
    # Generate all valid 3-digit even numbers from the digits
    for hundred in range(1, 10):  # First digit can't be 0
        if count[hundred] <= 0:
            continue
            
        # Use this digit
        count[hundred] -= 1
        
        for ten in range(10):  # Second digit can be any digit
            if count[ten] <= 0:
                continue
                
            # Use this digit
            count[ten] -= 1
            
            for unit in range(0, 10, 2):  # Last digit must be even
                if count[unit] <= 0:
                    continue
                    
                # Form the number
                num = hundred * 100 + ten * 10 + unit
                result.add(num)
                
            # Restore second digit count
            count[ten] += 1
            
        # Restore first digit count
        count[hundred] += 1
    
    return sorted(list(result))

def findEvenNumbers(digits):
    """
    Brute Force
    """
    res = []
    count = Counter(digits)
    for num in range(100, 1000):
        if num % 2 == 0:
            ok = True  # Fixed logic bug: Start with True and set to False if any condition fails
            num_digit_count = defaultdict(int)
            for d in str(num):
                num_digit_count[int(d)] += 1
            
            # Check if all digits in the number can be formed using the available digits
            for d, freq in num_digit_count.items():
                if count[d] < freq:
                    ok = False
                    break
                    
            if ok:
                res.append(num)
    return res

print(findEvenNumbers([2,1,3,0]))