import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	np.random.seed(seed)
	
	arr = np.arange(len(y))

	np.random.shuffle(arr)
	
	
	return X[arr], y[arr]