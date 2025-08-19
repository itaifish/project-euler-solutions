from math import comb
from time import perf_counter

start = perf_counter()
# the idea here is that what you are choosing isn't the "left" or the "down" directions,
# but instead the 20 (out of 40) positions that will be "left". Since you're just choosing
# the positions, the order doesn't matter, and so this is just 2*x choose x
result = comb(40, 20)
end = perf_counter()
print(result)
print(end - start)
