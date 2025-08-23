from itertools import permutations
from time import perf_counter

start = perf_counter()

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(permutations(digits))
millionth = ''.join(map(str, perms[1_000_000 - 1]))
end = perf_counter()
print(millionth)
print(end - start)