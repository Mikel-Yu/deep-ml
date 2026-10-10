
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	TP = 0
	FP = 0
	FN = 0

	for y_t, y_p in zip(y_true, y_pred):
		if y_t == 1 and y_p == 1:
			TP += 1
		elif y_t == 0 and y_p == 1:
			FP += 1
		elif y_t == 1 and y_p == 0:
			FN += 1
	
	if 2 * TP + FP + FN == 0:
		return 0

	res = 2 * TP / (2 * TP + FP + FN)
	return round(res, 3)
