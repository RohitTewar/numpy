import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("basic slicing",arr[2:7])
print("with step",arr[1:8:2])
print("negative indexing",arr[-3])

arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print("specific element",arr_2d[1,1])
print("entire row", arr_2d[2])  # Accessing element at row 1, column 2)
print("entire column", arr_2d[:,0])  # Accessing element at row 1, column 2)
