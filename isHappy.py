"""
202. Happy Number
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:

1 <= n <= 2^(31 - 1)
"""
def isHappy(n):
	# Solution 1: Using Dictionary
	# num = str(n)
	# total = {}
	# total[num] = 0
	# curr_total = 0
	# while True:
	# 	for c in num:
	# 		total[num] += int(c) ** 2        
	# 	curr_total = total[num]
	# 	if curr_total == 1:
	# 		return True
	# 	num = str(curr_total)
	# 	if num in total:
	# 		return False
	# 	total[num] = 0
    
	# Solution 2: Using Set    
	def get_next(number):
		total_sum = 0
		while number > 0:
			digit = number % 10
			total_sum += digit ** 2
			number //= 10
		return total_sum

	seen = set()
	while n != 1 and n not in seen:
		seen.add(n)
		n = get_next(n)

	return n == 1


print(isHappy(19))
print(isHappy(2))