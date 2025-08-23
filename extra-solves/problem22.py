from time import perf_counter


start = perf_counter()
a_val_minus_one = 64  # ord('A') - 1


def solve(file_name: str):
	names_file = open(file_name, "r")
	names_full_str = names_file.read()
	names = list(map(lambda str: str[1:-1], names_full_str.split(",")))
	names.sort()

	total_sum = 0
	for i in range(len(names)):
		name = names[i]
		letter_val = 0
		for letter in name:
			letter_val += ord(letter) - a_val_minus_one
		total_sum += (i + 1) * letter_val
	return total_sum


result = solve("resources/0022_names.txt")
end = perf_counter()
print(result)
print(end - start)
