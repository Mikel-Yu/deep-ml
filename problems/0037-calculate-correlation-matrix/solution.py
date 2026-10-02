import numpy as np

def calculate_correlation_matrix(X, Y=None):
    X = np.asarray(X)
    if Y is None:
        return np.corrcoef(X, rowvar=False)
    
    Y = np.asarray(Y)
    
    # Get the full joint correlation matrix (size: (cols_X + cols_Y) x (cols_X + cols_Y))
    full_corr = np.corrcoef(X, Y, rowvar=False)
    
    num_cols_X = X.shape[1] if X.ndim > 1 else 1
    num_cols_Y = Y.shape[1] if Y.ndim > 1 else 1
    
    # Extract the upper-right block: correlation between X variables and Y variables
    return full_corr[:num_cols_X, num_cols_X:]