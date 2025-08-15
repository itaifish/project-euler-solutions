# https://projecteuler.net/problem=12
from math import floor, sqrt
from typing import Dict, List

prime_factors_dict: Dict[int, List[int]] = {}

def prime_factors_for_num(number: int):
	if prime_factors_dict.get(number) != None:
		return prime_factors_dict[number]
	factors = []
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

def count_divisors_from_prime_factors(prime_factors: List[int]):
	sorted_factors = sorted(prime_factors)
	last_num = -1
	running_total_count = 0
	running_total_divisors = 1
	for factor in sorted_factors:
		if factor == last_num:
			running_total_count += 1
		else:
			running_total_divisors *= running_total_count + 1
			running_total_count = 1
			last_num = factor
	running_total_divisors *= running_total_count + 1
	return running_total_divisors



def first_triangle_number_with_divisors(num_divisors_min: int):
	triangle_number = 0
	position = 0
	while True:
		position += 1
		triangle_number += position
		prime_factors = prime_factors_for_num(triangle_number)
		divisors = count_divisors_from_prime_factors(prime_factors)
		# print("{triangle_number} has {divisors} divisors [{prime_factors}]".format(triangle_number=triangle_number, divisors=divisors, prime_factors=prime_factors))
		if divisors >= num_divisors_min:
			return triangle_number

triangle_num = 72
#prime_factors = prime_factors_for_num(triangle_num) 
#print(prime_factors)
#print(count_divisors_from_prime_factors(prime_factors))

print(first_triangle_number_with_divisors(501))