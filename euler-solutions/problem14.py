# https://projecteuler.net/problem=14

from typing import Dict, List

collatz_memoized: Dict[int, int] = {1: 1}


def find_collatz_length(num: int):
	# list of numbers and their offsets to add
	if collatz_memoized.get(num) is not None:
		return collatz_memoized[num]
	if num & 1 == 0:
		collatz_memoized[num] = 1 + find_collatz_length(int(num / 2))
	else:
		collatz_memoized[num] = 1 + find_collatz_length((3 * num) + 1)
	return collatz_memoized[num]


def find_largest_collatz_sequence_within_range(max_num: int):
	running_max = 1
	number_for_length = 1
	for i in range(2, max_num + 1):
		new_len = find_collatz_length(i)
		if new_len > running_max:
			running_max = new_len
			number_for_length = i
	return number_for_length


print(find_largest_collatz_sequence_within_range(1000000))
