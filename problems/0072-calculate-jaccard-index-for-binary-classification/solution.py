
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	intersect = 0
	union = 0

	for y_t, y_p in zip(y_true, y_pred):
		if y_t == 1 and y_p == 1:
			intersect += 1
		if y_t == 1 or y_p == 1:
			union += 1

	result = intersect / union
	return round(result, 3)
