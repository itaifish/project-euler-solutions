from time import perf_counter

start = perf_counter()

# 0-9
words_dict_digits_fast = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]
# 20-90
words_dict_tens_fast = [-1, -1, 6, 6, 5, 5, 5, 7, 6, 6]

hundred = 7
one_thousand = 11
and_word = 3

# 10-19
words_dict_special_fast = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

all_nums = [0] * 1001

for i in range(10):
	all_nums[i] = words_dict_digits_fast[i]
	all_nums[i + 10] = words_dict_special_fast[i]
	if i > 1:
		all_nums[i * 10] = words_dict_tens_fast[i]
all_nums[1000] = one_thousand


def number_to_letter_count(num: int):
	if all_nums[num] != 0:
		return all_nums[num]
	if num >= 100:
		result, remainder = divmod(num, 100)
		hundreds_piece = all_nums[result] + hundred
		if remainder > 0:
			res = hundreds_piece + and_word + all_nums[remainder]
			all_nums[num] = res
			return res
		all_nums[num] = hundreds_piece
		return hundreds_piece
	# num is always >= 20 since we pre-compute the first 20 as theyre special
	result, remainder = divmod(num, 10)
	extra = 0 if remainder == 0 else all_nums[remainder]
	res = words_dict_tens_fast[result] + extra
	all_nums[num] = res
	return res


def solve():
	total = 0
	for i in range(1, 1001):
		total += number_to_letter_count(i)
	return total


result = solve()
end = perf_counter()
print(result)
print(end - start)
