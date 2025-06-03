#sorting in numpy
import numpy as np
unsorted = np.array([3, 1, 4, 2, 5, 8, 1, 0, 6, 9, 7])
print("sorted array:", np.sort(unsorted))

arr_2d_unsorted = np.array([[3, 1, 4],
                           [2, 5, 8],
                           [1, 0, 6],
                           [9, 7, 3]])
print("sorted 2d array:",np.sort(arr_2d_unsorted,axis=0))