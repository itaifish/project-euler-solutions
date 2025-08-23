# https://projecteuler.net/problem=21
from itertools import combinations
from math import sqrt
from time import perf_counter
from typing import Dict, List

start = perf_counter()

prime_factors_dict: Dict[int, List[int]] = {}
sum_of_divisors_dict: Dict[int, int] = {}

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

def is_amicable_number(num: int):
	divisor_sum = sum_of_proper_divisors(num)
	if num == divisor_sum:
		return False
	amicable_sum = sum_of_proper_divisors(divisor_sum)
	return num == amicable_sum

def solve(max: int):
	sum = 0
	for i in range(max):
		if is_amicable_number(i):
			sum += i
	return sum
result = solve(10_000)
end = perf_counter()
print(result)
print(end - start)
