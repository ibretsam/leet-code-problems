"""
273. Integer to English Words
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 2^31 - 1
"""
def numberToWords(num):
	res = []
	num_to_word_map = {
		0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
		8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
		15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
		30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
		100: "One Hundred"
	}

	unit_to_word_map = {
		100: "Hundred",
		1000: "Thousand",
		1000000: "Million",
		1000000000: "Billion"
	}

	if num in num_to_word_map:
		return num_to_word_map[num]    
	multiplier = int("1" + "".join(["0" for _ in range(len(str(num)) - 1)]))

	while num:
		if num in num_to_word_map:
			res.append(num_to_word_map[num])
			break
		if multiplier < 100:
			res.append(num_to_word_map[10 * (num // 10)])
			res.append(num_to_word_map[num % 10])
			break
		curr_num = num // multiplier
		while multiplier not in unit_to_word_map:
			multiplier //= 10
			curr_num = num // multiplier
		if curr_num not in num_to_word_map:
			num_str = numberToWords(curr_num)
			curr_num_char = num_str + " " + unit_to_word_map[multiplier]
		else:
			curr_num_char = num_to_word_map[curr_num] + " " + unit_to_word_map[multiplier]
		if curr_num != 0:
			res.append(curr_num_char)
		num %= multiplier
		multiplier //= 10
	return " ".join(res)


# Test cases
print(numberToWords(1099))  # "One Thousand Ninety Nine"
print(numberToWords(323))  # "Three Hundred Twenty Three"
print(numberToWords(1412)) # "One Thousand Four Hundred Twelve"
print(numberToWords(1422))  # "One Thousand Four Hundred Twenty Two"
print(numberToWords(12345))  # "Twelve Thousand Three Hundred Forty Five"
print(numberToWords(1234567))  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
