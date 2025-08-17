words_dict_digits = {
	0: 4,  # "zero"
	1: 3,  # "one",
	2: 3,  # "two",
	3: 5,  # "three",
	4: 4,  # "four",
	5: 4,  # "five",
	6: 3,  # "six",
	7: 5,  # "seven",
	8: 5,  # "eight",
	9: 4,  # "nine",
}

words_dict_tens = {
	20: 6,  # twenty
	30: 6,  # thirty
	40: 5,  # forty
	50: 5,  # fifty
	60: 5,  # sixty
	70: 7,  # seventy
	80: 6,  # eighty
	90: 6,  # ninety
}

hundred = 7
one_thousand = 11
and_word = 3

words_dict_special = {
	10: 3,  # ten
	11: 6,  # "eleven"
	12: 6,  # "twelve"
	13: 8,  # "thirteen"
	14: 8,  # fourteen
	15: 7,  # fifteen
	16: 7,  # sixteen
	17: 9,  # seventeen
	18: 8,  # eighteen
	19: 8,  # nineteen
	1000: 11,  # one thousand
}


def number_to_letter_count(num: int, is_root=True):
	if not is_root and num == 0:
		return 0
	if words_dict_special.get(num) is not None:
		return words_dict_special[num]
	if num >= 100:
		result, remainder = divmod(num, 100)
		hundreds_piece = number_to_letter_count(result, False) + hundred
		if remainder > 0:
			return hundreds_piece + and_word + number_to_letter_count(remainder, False)
		return hundreds_piece
	if num >= 20:
		result, remainder = divmod(num, 10)
		return words_dict_tens[result * 10] + number_to_letter_count(remainder, False)
	else:
		return words_dict_digits[num]


total = 0
for i in range(1, 1001):
	total += number_to_letter_count(i)
print(total)
