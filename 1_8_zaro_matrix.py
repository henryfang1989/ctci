# question: write a algorithm such that if an element in an M8N matrix is 0, its entire column are set to 0

def zero_matrix(grid):
	rows = set()
	cols = set()

	# find all rows and cols
	for i in xrange(len(grid)):
		for j in xrange(len(grid[0])):
			if grid[i][j] == 0:
				rows.add(i)
				cols.add(j)

	# set rows
	for i in rows:
		for j in xrange(len(grid[0])):
			grid[i][j] = 0

	# set cols
	for j in cols:
		for i in xrange(len(grid)):
			grid[i][j] = 0

	return grid

# time: O(M*N)
# space: O(M+N)

grid1 = [
	[1,2,3,4],
	[5,6,0,8]
	]

grid2 = [
	[1,2,3,4],
	[5,6,0,8],
	[1,2,2,2]
	]

grid3 = []

print zero_matrix(grid1)

print zero_matrix(grid2)

print zero_matrix(grid3)

# solution to reduce the space to O(1)
# use first row and first col to save the status of current row and col to be set as zeros

def zero_matrix2(grid):
	if not grid or not grid[0]:
		return grid

	first_col_has_zero = first_row_has_zero = False

	for i in xrange(len(grid)):
		if grid[i][0] == 0:
			first_col_has_zero = True

	for j in xrange(len(grid[0])):
		if grid[0][j] == 0:
			first_row_has_zero = True

	for i in xrange(1, len(grid)):
		for j in xrange(1, len(grid[0])):
			if grid[i][j] == 0:
				grid[i][0] = 0
				grid[0][j] = 0

	for i in xrange(1, len(grid)):
		if grid[i][0] == 0:
			for j in xrange(len(grid[0])):
				grid[i][j] = 0

	for j in xrange(1, len(grid[0])):
		if grid[0][j] == 0:
			for i in xrange(len(grid)):
				grid[i][j] = 0

	if first_col_has_zero:
		for i in xrange(len(grid)):
			grid[i][0] = 0

	if first_row_has_zero:
		for j in xrange(len(grid[0])):
			grid[0][j] = 0

	return grid


grid1 = [
	[1,2,3,4],
	[5,6,0,8]
	]

grid2 = [
	[1,2,3,4],
	[5,6,0,8],
	[1,2,2,2]
	]

grid3 = []

grid4 = [
	[1,1,2,3],
	[0,5,6,7],
	[8,9,10,11]
	]
# time: O(M*N)
# space: O(1) because we reuse the grid
print zero_matrix2(grid1)

print zero_matrix2(grid2)

print zero_matrix2(grid3)

print zero_matrix2(grid4)
