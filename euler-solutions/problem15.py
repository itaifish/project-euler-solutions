from math import comb
from time import perf_counter

start = perf_counter()
result = comb(40, 20)
end = perf_counter()
print(result)
print(end - start)
