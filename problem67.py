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


triangle_file = open("resources/0067_triangle.txt", "r")
triangle = triangle_file.readlines()
lists = list(map(lambda string_list: list(map(int, string_list.split())), triangle))
best_path_solution = [[-1 for _ in num_list] for num_list in lists]
best_path_solution[0][0] = lists[0][0]
for list_index in range(1, len(lists)):
	num_list = lists[list_index]
	for item_index in range(len(num_list)):
		best_path_solution[list_index][item_index] = num_list[item_index] + max(
			get_or_none(best_path_solution, list_index - 1, item_index - 1) or 0,
			get_or_none(best_path_solution, list_index - 1, item_index) or 0,
		)
print(max(best_path_solution[len(lists) - 1]))
