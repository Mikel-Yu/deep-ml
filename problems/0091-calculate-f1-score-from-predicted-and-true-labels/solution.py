def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
	TP = 0
	FP = 0
	FN = 0

	for y_t, y_p in zip(y_true, y_pred):
		if y_t == 1 and y_p == 1:
			TP += 1
		elif y_t == 1 and y_p == 0:
			FP += 1
		elif y_t == 0 and y_p == 1:
			FN += 1
	

	if TP + FP == 0 or TP + FN == 0:
		return 0.0

	precision = TP / (TP + FP)
	recall = TP / (TP + FN)
	f1 = 2 * precision * recall / (precision + recall)
	return round(f1,3)