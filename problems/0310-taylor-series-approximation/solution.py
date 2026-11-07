import numpy as np
from math import factorial

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    """
    Compute Taylor series approximation for common functions.
    
    Args:
        func_name: Name of function ('exp', 'sin', 'cos')
        x: Point at which to evaluate
        n_terms: Number of terms in the series
    
    Returns:
        Taylor series approximation rounded to 6 decimal places
    """
    n = np.arange(n_terms)
    fac = np.vectorize(factorial)
    if func_name == "exp":
        return np.sum((x ** n) / fac(n))
    elif func_name == "sin":
        return np.sum(((-1) ** n * x ** (2 * n + 1)) / fac(2 * n + 1))
    elif func_name == "cos":
        return np.sum(((-1) ** n * x ** (2 * n)) / fac(2 * n))