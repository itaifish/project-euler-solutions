f = open("resources/0081_matrix.txt")

matrix = list(map(lambda x: list(map(int, x.split(","))), f.readlines()))

size = len(matrix)

# do first iteration

for i in range(1, size):
	matrix[0][i] += matrix[0][i - 1]
	matrix[i][0] += matrix[i - 1][0]
	
# now, starting at 1,1, we have options - take the min of left vs up and add

for i in range(1, size):
	x = i
	y = i
	matrix[x][y] += min(matrix[y - 1][x], matrix[y][x - 1])
	for j in range(1, size - i):
		matrix[y][x + j] += min(matrix[y - 1][x + j], matrix[y][x + j - 1])
		matrix[y + j][x] += min(matrix[y + j][x - 1], matrix[y + j - 1][x])



print(matrix[-1][-1])
