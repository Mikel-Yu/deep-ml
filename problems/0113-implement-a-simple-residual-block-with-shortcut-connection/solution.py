import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    # Your code here
    # 1. multiply with w1
    result = w1 @ x

    # 2. result
    result = np.maximum(result, 0)

    # 3. multiply with w2
    result = w2 @ result

    # 4. add x
    result += x

    # 5. final ReLU
    result = np.maximum(result, 0)

    return result

    
