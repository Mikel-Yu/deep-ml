from math import exp

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	sigmoid = 1 / (1 + exp(-x))
	sigmoid_deriv = sigmoid * (1 - sigmoid)

	tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
	tanh_deriv = 1 - tanh ** 2

	relu_deriv = 1 if x > 0 else 0
	
	result = {
		'sigmoid' : sigmoid_deriv,
		'tanh' : tanh_deriv,
		'relu' : relu_deriv
	}

	return result