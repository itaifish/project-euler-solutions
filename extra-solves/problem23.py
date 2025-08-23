from itertools import combinations, combinations_with_replacement
from math import sqrt
from time import perf_counter
from typing import Dict, List

start = perf_counter()

prime_factors_dict: Dict[int, List[int]] = {}
sum_of_divisors_dict: Dict[int, int] = {}

max_to_check = 28122


def prime_factors_for_num(number: int):
	if prime_factors_dict.get(number) != None:
		return prime_factors_dict[number]
	factors: List[int] = []
	finished = False
	cur_number = number
	while not finished:
		i = 2
		max = sqrt(cur_number)
		while i <= max:
			result, remainder = divmod(cur_number, i)
			if remainder == 0:
				factors += prime_factors_for_num(i)
				cur_number = int(result)
				break
			i += 1
		if i >= max:
			finished = True
	prime_factors_dict[cur_number] = [cur_number]
	factors.append(cur_number)
	prime_factors_dict[number] = factors
	return factors


def get_divisors_from_prime_factors(prime_factors: List[int]):
	divisors: set[int] = set()
	for i in range(len(prime_factors)):
		combos = combinations(prime_factors, i)
		for combo in combos:
			divisor = 1
			for number in combo:
				divisor *= number
			divisors.add(divisor)
	return divisors


def sum_of_proper_divisors(num: int):
	lookup = sum_of_divisors_dict.get(num)
	if lookup is not None:
		return lookup
	res = sum(get_divisors_from_prime_factors(prime_factors_for_num(num)))
	sum_of_divisors_dict[num] = res
	return res


def is_abundant(num: int):
	sum_of_divisors = sum_of_proper_divisors(num)
	return sum_of_divisors > num


def get_all_abundant_numbers_to_max(num: int):
	return [i for i in range(12, num + 1) if is_abundant(i)]


def solve():
	abundant_nums = get_all_abundant_numbers_to_max(max_to_check)
	sums = set(
		map(
			lambda tuple: tuple[0] + tuple[1],
			combinations_with_replacement(abundant_nums, 2),
		)
	)
	total = 0
	for i in range(1, max_to_check):
		if i not in sums:
			total += i
	return total


res = solve()
end = perf_counter()
print(res)
print(end - start)
