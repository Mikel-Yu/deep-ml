import numpy as np

def calculate_brightness(img):
	# Write your code here
	# Catches jagged arrays
	try:
		img = np.array(img)
	except ValueError:
		return -1

	if img.size == 0: # Empty
		return -1
	elif np.any((img < 0) | (img > 255)): # Invalid values
		return -1
	
	return np.mean(img)

