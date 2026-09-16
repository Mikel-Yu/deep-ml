import math

def sigmoid(z: float) -> float:
    # Numerically stable sigmoid function
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    else:
        exp_z = math.exp(z)
        return exp_z / (1.0 + exp_z)

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here

	z = [
        sum(f * w for f, w in zip(sample, weights)) + bias
        for sample in features
    ]

	probabilities = [round(sigmoid(zi), 4) for zi in z]

	mse = 1 / len(features) * sum((p - label)**2 for p, label in zip(probabilities, labels))
	
	return probabilities, mse