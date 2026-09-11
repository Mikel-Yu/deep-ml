import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
    """
    a_2 = np.transpose(A) @ A
    v = np.eye(2)
    
    if np.isclose(a_2[0, 0], a_2[1, 1]):
        theta = np.pi / 4
    else:
        theta = 0.5 * np.arctan2(2 * a_2[0, 1], (a_2[0, 0] - a_2[1, 1]))
        
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    v = v @ r
    
    d = np.transpose(r) @ a_2 @ r
    sigma_d = np.sqrt(np.maximum([d[0, 0], d[1, 1]], 0))
    
    sigma_inv = np.array([
        [1 / sigma_d[0] if sigma_d[0] > 1e-12 else 0, 0],
        [0, 1 / sigma_d[1] if sigma_d[1] > 1e-12 else 0]
    ])
    
    u = A @ v @ sigma_inv
    
    return (u, sigma_d, v.T)