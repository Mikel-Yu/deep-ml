from math import sqrt

def phi_corr(x: list[int], y: list[int]) -> float:
    """
    Calculate the Phi coefficient between two binary variables.

    Args:
    x (list[int]): A list of binary values (0 or 1).
    y (list[int]): A list of binary values (0 or 1).

    Returns:
    float: The Phi coefficient rounded to 4 decimal places.
    """
    # Your code here
    x00, x01, x10, x11 = 0, 0, 0, 0

    for X, Y in zip(x, y):
        if X == 0 and Y == 0:
            x00 += 1
        elif X == 0 and Y == 1:
            x01 += 1
        elif X == 1 and Y == 0:
            x10 += 1
        else:
            x11 += 1
    
    numerator = ((x00 * x11) - (x01 * x10))
    denominator = sqrt((x00 + x01) * (x10 + x11) * (x00 + x10) * (x01 + x11))

    if denominator == 0:
        return 0.0

    val = numerator / denominator 


    return round(val,4)