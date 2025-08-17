from math import factorial
from time import perf_counter


def solve():
	num = factorial(100)
	return sum(map(int, list(str(num))))


start = perf_counter()
result = solve()
end = perf_counter()
print(result)
print(end - start)
