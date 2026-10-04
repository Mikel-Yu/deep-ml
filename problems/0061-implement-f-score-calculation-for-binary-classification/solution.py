import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp = 0
	fp = 0
	fn = 0

	for y_t, y_p in zip(y_true, y_pred):
		if y_t == 1 and y_p == 1:
			tp += 1
		elif y_t == 0 and y_p == 1:
			fp += 1
		elif y_t == 1 and y_p == 0:
			fn += 1
	
	r = tp / (tp + fn)
	p = tp / (tp + fp)

	return round((1 + beta ** 2) * (p * r) / ((beta ** 2 * p) + r), 3)
