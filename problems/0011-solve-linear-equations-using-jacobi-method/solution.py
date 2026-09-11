import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

	D = np.diag(A) # D is now 1D
	R = A - np.diag(D) # D is now 2D
	x = np.zeros(len(b))

	for _ in range(n):
		x_new = 1/D * (b - R @ x)
		x = x_new

	return x