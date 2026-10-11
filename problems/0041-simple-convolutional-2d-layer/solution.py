import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	# Your code here
	padded = np.pad(input_matrix, 
					pad_width=((padding, padding), (padding, padding)),
					mode='constant', 
					constant_values=0)
	
	input_height, input_width = padded.shape
	oh = (input_height - kernel_height) // stride + 1
	ow = (input_width - kernel_width) // stride + 1

	output_matrix = np.zeros((oh, ow), dtype=np.float64)

	for i in range(oh):
		for j in range(ow):
			start_i = i * stride
			start_j = j * stride
			region = padded[start_i:start_i+kernel_height, start_j:start_j+kernel_width]
			output_matrix[i, j] = np.sum(region * kernel)
    
	return output_matrix
