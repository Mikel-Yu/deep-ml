import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    X = np.array(input_sequence)
    h = np.array(initial_hidden_state)
    Wx = np.array(Wx)
    Wh = np.array(Wh)
    b = np.array(b)

    for x_t in X:
        # If Wx and Wh are 2D matrices, use proper matrix multiplication (@)
        if Wx.ndim == 2 and Wh.ndim == 2:
            # Ensure dimensions match for matrix multiplication
            if x_t.ndim == 1:
                x_t = x_t.reshape(-1, 1)
            if h.ndim == 1:
                h = h.reshape(-1, 1)
            if b.ndim == 1:
                b = b.reshape(-1, 1)
                
            h = np.tanh(Wx @ x_t + Wh @ h + b)
        else:
            # Fallback to scalar/element-wise multiplication for 1D/scalar test cases
            h = np.tanh(Wx * x_t + Wh * h + b)

    final_hidden_state = np.atleast_1d(h).flatten().tolist()
    return [round(float(val), 4) for val in final_hidden_state]