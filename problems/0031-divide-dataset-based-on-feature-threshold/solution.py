import numpy as np

def divide_on_feature(X, feature_i, threshold):
	# Your code here
	ge, less = [], []
	for x in X:
		if x[feature_i] >= threshold:
			ge.append(x)
		else:
			less.append(x)
	return [np.array(ge), np.array(less)]