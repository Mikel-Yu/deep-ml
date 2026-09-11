def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    if not values:
        return []

    encoding = []

    for value in values:
        for num in order:
            if value == num:
                encoding.append(order.index(num))
        if value not in order:
            encoding.append(-1)

    return encoding