import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	mse = np.mean((X @ w - y_true) ** 2)
	reg = alpha * sum(w**2)
	return mse + reg
