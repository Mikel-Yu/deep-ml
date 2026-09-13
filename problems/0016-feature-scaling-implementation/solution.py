import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	std = np.std(data, axis=0)
	range_val = np.ptp(data, axis=0)  # np.max(data, axis=0) - np.min(data, axis=0)

	std = np.where(std == 0, 1.0, std)
	range_val = np.where(range_val == 0, 1.0, range_val)

	standardized_data = (data - np.mean(data, axis=0)) / std
	normalized_data = (data - np.min(data, axis = 0)) / range_val

	return standardized_data, normalized_data