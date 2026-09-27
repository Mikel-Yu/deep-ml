import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	updated_weights = initial_weights
	updated_bias = initial_bias
	mse_values = []

	n_samples = features.shape[0]

	for _ in range(epochs):
		z = np.dot(features, updated_weights) + updated_bias
		sigmoid = 1 / (1 + np.exp(-z))

		mse_values.append(np.mean((sigmoid - labels) ** 2))

		err = sigmoid - labels
		sigmoid_deriv = sigmoid * (1 - sigmoid)
		delta = err * sigmoid_deriv

		w_grad = 2 / n_samples * np.dot(features.T, delta)
		b_grad = 2 / n_samples * np.sum(delta)

		updated_weights -= learning_rate * w_grad
		updated_bias -= learning_rate * b_grad

	return np.round(updated_weights, 4).tolist(), np.round(updated_bias, 4), np.round(mse_values, 4).tolist()