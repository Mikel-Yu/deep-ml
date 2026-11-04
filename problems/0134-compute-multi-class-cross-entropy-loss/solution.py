import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    # Your code here
    predicted_probs = np.clip(predicted_probs, epsilon, 1 - epsilon)
    L_batch = np.mean(np.sum(-true_labels * np.log(predicted_probs), axis=1))
    return L_batch