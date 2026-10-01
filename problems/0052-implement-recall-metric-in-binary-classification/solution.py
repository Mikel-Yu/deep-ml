import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    tp = 0
    fn = 0

    for y_t, y_p in zip(y_true, y_pred):
        if y_t == 1 and y_p == 1:
            tp += 1
        elif y_t == 1 and y_p == 0:
            fn += 1
    
    # Division by 0
    if tp + fn == 0:
        return 0
    return tp / (tp + fn)
