
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	SSR = np.sum((y_true - y_pred) ** 2)
	SST = np.sum((y_true - np.mean(y_pred)) ** 2)
	
	return 1 - SSR / SST
