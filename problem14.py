# https://projecteuler.net/problem=14

from typing import Dict, List

collatz_memoized: Dict[int, int] = {1: 1}


def find_collatz_length(num: int):
	curr_num = num
	# list of numbers and their offsets to add
	to_add: List[int] = []
	while collatz_memoized.get(curr_num) is None:
		to_add.append(curr_num)
		if curr_num & 1 == 0:
			curr_num = int(curr_num / 2)
		else:
			curr_num = (curr_num * 3) + 1
	offset_to_add = collatz_memoized[curr_num]
	for index in range(len(to_add) - 1, -1, -1):
		true_offset = len(to_add) - index
		collatz_memoized[to_add[index]] = true_offset + offset_to_add
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
