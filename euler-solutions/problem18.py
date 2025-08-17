from time import perf_counter
from typing import List, TypeVar

T = TypeVar("T")


def get_or_none(
	list: List[List[T]] | List[T] | None, index: int, inner_index: int | None = None
):
	if inner_index is not None:
		return get_or_none(get_or_none(list, index), inner_index)
	if list is None:
		return None
	if index >= len(list):
		return None
	return list[index]


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


def solve():
	lists = list(
		map(
			lambda string_list: list(map(int, string_list.split())),
			triangle.split("\n"),
		)
	)
	best_path_solution = [[-1 for _ in num_list] for num_list in lists]
	best_path_solution[0][0] = lists[0][0]
	for list_index in range(1, len(lists)):
		num_list = lists[list_index]
		for item_index in range(len(num_list)):
			best_path_solution[list_index][item_index] = num_list[item_index] + max(
				get_or_none(best_path_solution, list_index - 1, item_index - 1) or 0,
				get_or_none(best_path_solution, list_index - 1, item_index) or 0,
			)
	return max(best_path_solution[len(lists) - 1])


start = perf_counter()
result = solve()
end = perf_counter()
print(result)
print(end - start)
