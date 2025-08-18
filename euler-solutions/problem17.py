from time import perf_counter
# 0-9
words_dict_digits_fast = [4,3,3,5,4,4,3,5,5,4]
#20-90
words_dict_tens_fast = [-1, -1, 6, 6, 5, 5, 5, 7, 6, 6]

hundred = 7
one_thousand = 11
and_word = 3

# 10-19
words_dict_special_fast = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]


def number_to_letter_count(num: int, is_root=True):
	if not is_root and num == 0:
		return 0
	if num == 1_000:
		return one_thousand
	teens_index = num - 10
	if teens_index >= 0 and teens_index < len(words_dict_special_fast):
		return words_dict_special_fast[teens_index]
	if num >= 100:
		result, remainder = divmod(num, 100)
		hundreds_piece = number_to_letter_count(result, False) + hundred
		if remainder > 0:
			return hundreds_piece + and_word + number_to_letter_count(remainder, False)
		return hundreds_piece
	if num >= 20:
		result, remainder = divmod(num, 10)
		return words_dict_tens_fast[result] + number_to_letter_count(remainder, False)
	else:
		return words_dict_digits_fast[num]


def solve():
	total = 0
	for i in range(1, 1001):
		total += number_to_letter_count(i)
	return total


start = perf_counter()
result = solve()
end = perf_counter()
print(result)
print(end - start)
