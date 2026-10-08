
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	mse = np.mean((y_true - y_pred) ** 2)
	rmse_res = np.sqrt(mse)

	return np.round(rmse_res,3)
