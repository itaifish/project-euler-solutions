from math import floor, log, sqrt

sqrt_5 = sqrt(5)
golden_ratio = (1 + sqrt_5) / 2
log_of_sqrt_5_base_golden_ratio = log(sqrt_5, golden_ratio)
log_of_golden_ratio_base_10 = log(golden_ratio, 10)
log_of_sqrt_5_base_10 = log(sqrt_5, 10)


def index_of_fib(fib_num: int):
	return round(log(fib_num, golden_ratio) + log_of_sqrt_5_base_golden_ratio)


def num_digits_of_nth_fib_number(n: int):
	# essentially we use the general theory of how to get the number of digits of *any* number:
	# 1 + floor(log_10(num))
	# then we apply the math -> 1 + floor(log_10(fib(n)))
	# which turns into -> 1 + floor(log_10((golden_ratio**num) / sqrt_5))
	# using log division rules we get -> 1 + floor(log_10((golden_ratio**num)) - log_10(sqrt_5))
	# using log power rules we get -> 1 + floor(num*log_10(golden_ratio) - log_10(sqrt_5))
	return 1 + floor(n * log_of_golden_ratio_base_10 - log_of_sqrt_5_base_10)


def fib(num: int):
	fib_unrounded = (golden_ratio**num) / sqrt_5
	return round(fib_unrounded)


def find_first_fib_number_with_n_digits(digits: int):
	smallest_num_of_n_digits = 10 ** (digits - 1)
	index_of_first_guess = index_of_fib(smallest_num_of_n_digits)
	digits_of_first_guess = num_digits_of_nth_fib_number(index_of_first_guess)
	if digits_of_first_guess == digits:
		return index_of_first_guess
	return index_of_first_guess + 1


index = find_first_fib_number_with_n_digits(1000)
print(index)

# we test out code
for i in range(2, 1000):
	fib_res = fib(i)
	real_answer = len(str(fib_res))
	computed_answer = num_digits_of_nth_fib_number(i)
	if real_answer != computed_answer:
		print(f"{real_answer} != {computed_answer} for i of {i} [{fib_res}]")
	computed_index = index_of_fib(fib_res)
	if i != computed_index:
		print(f"{computed_index} != {i} for i of {i} [{fib_res}]")
