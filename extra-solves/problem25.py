from math import floor, log, sqrt

sqrt_5 = sqrt(5)
golden_ratio = (1+sqrt_5)/2
golden_ratio_conjugate = (1-sqrt_5)/2
log_of_sqrt_5_base_golden_ratio = log(sqrt_5, golden_ratio)
log_of_golden_ratio_base_10 = log(golden_ratio, 10)

def index_of_fib(fib_num: int):
	return round(log(fib_num, golden_ratio) + log_of_sqrt_5_base_golden_ratio)

def num_digits_of_nth_fib_number(n: int):
	return 1 + floor(n*log_of_golden_ratio_base_10)

def fib(num: int):
	fib_unrounded = (golden_ratio**num) / sqrt_5
	return round(fib_unrounded)

def find_first_fib_number_with_n_digits(digits: int):
	smallest_num_of_n_digits = 10**(digits - 1)
	index_of_first_guess = index_of_fib(smallest_num_of_n_digits)
	digits_of_first_guess = num_digits_of_nth_fib_number(index_of_first_guess)
	if digits_of_first_guess == digits:
		# we could have overshot by 1, since we're trying to find the smallest possible, depending on rounding of course
		if num_digits_of_nth_fib_number(index_of_first_guess - 1) == digits:
			return index_of_first_guess - 1
		return index_of_first_guess
	return index_of_first_guess + 1

index = find_first_fib_number_with_n_digits(1000)
print(index)

print(fib(4782))