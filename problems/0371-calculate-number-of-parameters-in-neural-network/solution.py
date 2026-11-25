def calculate_parameters(layers: list[dict]) -> int:
    """
    Calculate the total number of trainable parameters in a neural network.

    Args:
        layers: List of dictionaries, each describing a layer.

    Returns:
        Total number of trainable parameters (int).
    """
    # Your code here
    params = 0
    for layer in layers:
        if layer['type'] == 'dense':
            if layer.get('bias', True):
                params += layer['input_size'] * layer['output_size'] + layer['output_size']
            else:
                params += layer['input_size'] * layer['output_size']
        else:
            if layer.get('bias', True):
                params += layer['in_channels'] * layer['out_channels'] * layer['kernel_size'] ** 2 + layer['out_channels']
            else:
                params += layer['in_channels'] * layer['out_channels'] * layer['kernel_size'] ** 2
    return params
