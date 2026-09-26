import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col == None:
		sort = np.unique(x)
		matrix = np.zeros((len(x), max(x)+1))
	else: 
		sort = np.arange(n_col)
		matrix = np.zeros((len(x), n_col))
	
	for i in range(len(matrix)): # rows
		for j in range(len(matrix[i])): # columns
			if x[i] == sort[j]:
				matrix[i][j] = 1

	return matrix 
