
memoized: dict[int, dict[int, int]] = {}

def get_choices(grid_size: int):
	def get_choices_helper(left_remaining: int, down_remaining: int):
		map_key1 = memoized.get(left_remaining)
		if map_key1 is None:
			memoized[left_remaining] = {}
			map_key1 = memoized.get(left_remaining)
		if map_key1.get(down_remaining):
			return map_key1[down_remaining]
		if left_remaining == 0 or down_remaining == 0:
			return 1
		result = get_choices_helper(left_remaining - 1, down_remaining) + get_choices_helper(left_remaining, down_remaining - 1)
		memoized[left_remaining][down_remaining] = result
		return result
	return get_choices_helper(grid_size, grid_size)


print(get_choices(20))