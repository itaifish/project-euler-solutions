# https://projecteuler.net/problem=14

from time import perf_counter
from typing import Dict

collatz_memoized: Dict[int, int] = {1: 1}


def find_collatz_length(num: int):
	# list of numbers and their offsets to add
	if collatz_memoized.get(num) is not None:
		return collatz_memoized[num]
	if num & 1 == 0:
		# if it is divisible by 4 we jump two steps
		if num & 3 == 0:
			collatz_memoized[num] = 2 + find_collatz_length(num >> 2)
		elif num > 4:
			# number is divisible by 2 but not 4. We can do even->odd->even->?
			# transformed_num = (3 * (num >> 1) + 1) >> 1 optimized to (3*num + 2) >> 2
			transformed_num = ((3 * num) + 2) >> 2
			collatz_memoized[num] = 3 + find_collatz_length(transformed_num)
		else:
			collatz_memoized[num] = 1 + find_collatz_length(num >> 1)
	else:
		# for odd we do 2 steps at once. since 3*odd + 1 will always be even
		collatz_memoized[num] = 2 + find_collatz_length(((3 * num) + 1) >> 1)
	return collatz_memoized[num]


def find_largest_collatz_sequence_within_range(max_num: int):
	running_max = 1
	number_for_length = 1
	for i in range(int(max_num / 2), max_num + 1):
		new_len = find_collatz_length(i)
		if new_len > running_max:
			running_max = new_len
			number_for_length = i
	return number_for_length


start = perf_counter()
result = find_largest_collatz_sequence_within_range(1_000_000)
end = perf_counter()
print(result)
print(end - start)
