import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    arr = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(arr)
    
    splits = np.array_split(arr, k)

    folds = []
    for i in range(k):
        test_indices = splits[i].tolist()
        train_indices = np.concatenate([splits[j] for j in range(k) if j != i]).tolist()
        folds.append((train_indices, test_indices))

    return folds