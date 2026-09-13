import numpy as np

def mutual_information(joint_prob: list[list[float]]) -> float:
	"""
	Compute the mutual information between two random variables.
	
	Args:
		joint_prob: 2D joint probability distribution P(X,Y)
	
	Returns:
		Mutual information I(X;Y)
	"""
	# Your code here
	P_XY = np.array(joint_prob)


	P_X = np.sum(joint_prob, axis=1)
	P_Y = np.sum(joint_prob, axis=0)

	P_X_P_Y = np.outer(P_X, P_Y)

	# Mask to avoid log(0) and division by zero
	mask = P_XY > 0

	I = np.sum(P_XY[mask] * np.log(P_XY[mask] / P_X_P_Y[mask]))

	return I