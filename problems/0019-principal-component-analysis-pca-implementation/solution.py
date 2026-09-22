import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    
    # 1. standardize
    data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # 2. Compute covariance matrix
    cov_matrix = np.cov(data.T)

    # 3. Find Eigenvalues and Eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix) # sorted ascending order
    
    # 4. Select top k eigenvectors in descending order of eigenvalues
    top_k_eigenvectors = eigenvectors[:, -k:][:, ::-1]

    # 5. Fix sign convention: make the first non-zero element positive for each column
    for col in range(k):
        v = top_k_eigenvectors[:, col]
        non_zero_idx = np.where(v != 0)[0]
        if len(non_zero_idx) > 0 and v[non_zero_idx[0]] < 0:
            top_k_eigenvectors[:, col] *= -1

    return np.round(top_k_eigenvectors, 4)

    # reverse order to descending
    return eigenvectors[-k:][::-1]
