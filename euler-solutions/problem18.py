from time import perf_counter
from typing import TypeVar

T = TypeVar("T")

start = perf_counter()


def get_from_list(list, index, inner_index):
	if index >= len(list) or inner_index >= len(list[index]):
		return 0
	return list[index][inner_index]


triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

lists = list(
	map(
		lambda string_list: list(map(int, string_list.split())),
		triangle.split("\n"),
	)
)


def solve(triangle):
	for row in range(len(triangle) - 2, -1, -1):
		for col in range(len(triangle[row])):
			l_parent = triangle[row + 1][col]
			r_parent = triangle[row + 1][col + 1]
			triangle[row][col] += l_parent if l_parent > r_parent else r_parent
	return triangle[0][0]


result = solve(lists)
end = perf_counter()
print(result)
print(end - start)
