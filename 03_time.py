import numpy as np
# Create a 1D list

py_list = [1, 2, 3]
print("list multiplication:",py_list*3)

np_list = np.array(py_list) #element wise multiplicaion
print("numpy list multiplication:",np_list*3)

import time
# Measure time taken for list multiplication
start_time = time.time()
py_list = [1, 2, 3] * 1000000
end_time = time.time()
print("\nTime taken for list multiplication:", end_time - start_time)

# Measure time taken for numpy array multiplication
start_time = time.time()
np_list = np.array([1,2,3,])*1000000
end_time = time.time()
print("\nTime taken for numpy array multiplication:", end_time - start_time)