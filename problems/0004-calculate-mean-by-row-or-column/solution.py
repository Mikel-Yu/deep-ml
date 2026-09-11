import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	matrix = np.array(matrix)
	means = []
	if mode == 'row':
		means = np.sum(matrix, axis = 1) / matrix.shape[1]
	else:
		means = np.sum(matrix, axis = 0) / matrix.shape [0]
			

	return means