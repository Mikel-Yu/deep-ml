import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here

	scores = np.array(scores)
	softmax = sum(np.exp(scores - max(scores)))

	log_softmax = scores - max(scores) - np.log(softmax)
	return log_softmax