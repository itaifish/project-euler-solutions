# https://projecteuler.net/problem=16

from time import perf_counter


def solve():
	power = 2**1000
	digit_sum = sum(map(int, list(str(power))))
	return digit_sum

start = perf_counter()
result = solve(40, 20)
end = perf_counter()
print(result)
print(end - start)


