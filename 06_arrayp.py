#properties of arrays

import numpy as np
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print("shape:", arr.shape)
print("dtype:", arr.dtype)
print("size:", arr.size)
print("dimension:", arr.ndim)

# array reshaping

arr = np.arange(10)
print("Original array:", arr)

reshaped = arr.reshape((2, 5))
print("Reshaped array:\n", reshaped)

flattened = reshaped.flatten()
print("Flattened array:", flattened)

#RAveling an array

reveled = reshaped.ravel()
print("Raveled array:", reveled)

# Transposing an array
transposed = reshaped.T 
print("Transposed array:\n", transposed)