import numpy as np

def determinant_4x4(matrix: list[list[int|float]]) -> float:
    arr = np.array(matrix, dtype=float)
    n = arr.shape[0]

    # Base case for recursion
    if n == 1:
        return float(arr[0, 0])
    if n == 2:
        return float(arr[0, 0] * arr[1, 1] - arr[0, 1] * arr[1, 0])

    det = 0.0
    # Laplace expansion along column 0
    for i in range(n):
        # Delete row i and column 0 to form the minor matrix
        minor = np.delete(np.delete(arr, i, axis=0), 0, axis=1)
        
        # Term = (-1)^(i+0) * element * det(minor)
        sign = (-1) ** i
        det += sign * arr[i, 0] * determinant_4x4(minor)

    return float(det)