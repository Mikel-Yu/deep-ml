import numpy as np

def disorder(apples: list) -> float:
    """
    Compute the disorder in a basket of apples.
    """
    # Your code here
    apples = np.array(apples)
    G = 1
    n = len(apples)

    for apple in np.unique(apples):
        G -= ((apples == apple).sum() / n) ** 2
    
    return G


    