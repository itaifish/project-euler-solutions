from time import perf_counter

start = perf_counter()
# 0-9
words_dict_digits_fast = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]
# 20-90
words_dict_tens_fast = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

hundred = 7
one_thousand = 11
and_word = 3

# 10-19
words_dict_special_fast = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
''' alternative solution if my main solution is ruled invalid

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
		# we don't actually need to save the hundreds piece since we don't go over 1000
		# all_nums[num] = hundreds_piece
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

'''

def solve_alternative():
	# for ten not including the second ten (teens) we have a set of ones, starting from 0 ten to 9 ten
	# so that's 9 per hundred times 10 hundreds = 90
	# but we also have the one hundred -> nine hundred, so add 100
	# since for each hundred we say all the numbers with that name
	one_to_nine = 190 * sum(words_dict_digits_fast[1:])
	# for each hundred we have a set of teens, starting from 0 hundred to 9 hundred inclusive (10 of them)
	ten_through_nineteen = 10 * sum(words_dict_special_fast)
	# for the tens we have this for every hundred, so 10 of them
	# and inside of every hundred, there are 10 (twenty->twentynine, thirty->thirtynine etc)
	tens = 100 * sum(words_dict_tens_fast[2:])
	#we say hundred for each number greater than or equal to 100, and not 1000, or 900 times (1001 (0 to 1000) minus 100 (0 -> 99) minus 1 (1000))
	hundreds = hundred * 900
	# we have an `and` for each number 100 or greater than doesn't end in a 00, or 99/100 of them
	# so 99/100 times 900, or 891
	# another way to think about it is for each hundred starting from the first, we add 99 
	# (ignoring xx hundred exactly, which has no and). So 99 * 9 = 891
	ands = and_word * 891

	return one_to_nine + ten_through_nineteen + tens + hundreds + ands + one_thousand


result = solve_alternative()

end = perf_counter()
print(result)
print(end - start)
