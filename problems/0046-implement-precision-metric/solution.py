import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = 0
	fp = 0

	for y_t, y_p in zip(y_true, y_pred):
		if y_t == 1 and y_p == 1:
			tp += 1
		elif y_t == 0 and y_p == 1:
			fp += 1

	if tp + fp == 0:
		return 0

	return tp / (tp + fp)
