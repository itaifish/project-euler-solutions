import re

words_dict_digits = {
	0: "zero",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
}

words_dict_tens = {
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
}

hundred = "hundred"
and_word = "and"

words_dict_special = {
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	1000: "one thousand",
}


def number_to_word(num: int, is_root=True):
	if not is_root and num == 0:
		return ""
	if words_dict_special.get(num) is not None:
		return words_dict_special[num]
	if num >= 100:
		result, remainder = divmod(num, 100)
		hundreds_piece = number_to_word(result, False) + " " + hundred
		if remainder > 0:
			return (
				hundreds_piece + " " + and_word + " " + number_to_word(remainder, False)
			)
		return hundreds_piece
	if num >= 20:
		result, remainder = divmod(num, 10)
		return words_dict_tens[result * 10] + "-" + number_to_word(remainder, False)
	else:
		return words_dict_digits[num]


total = ""
for i in range(1, 32):
	total += number_to_word(i) + "\n"
	stripped = re.sub(r"[\s\-\n]*", "", number_to_word(i))
stripped = re.sub(r"[\s\-\n]*", "", total)
print(len(stripped))
