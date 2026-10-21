import numpy as np

def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    x = np.array(x)

    x_prime = (x - np.min(x)) / (np.max(x) - np.min(x))
    return x_prime