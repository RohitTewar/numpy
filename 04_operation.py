#adding or removing a data
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

combined = np.concatenate((arr1, arr2))
print("Combined array:", combined)

#array compatibility

a= np.array([1, 2, 3])
b= np.array([4, 5, 6, 7])  # Note: b has an extra element
c= np.array([7, 8, 9])       

print("compatibility shape", a.shape == b.shape)

original = np.array([[1,2],[3,4]])
new_row = np.array([[5, 6]])
# Adding a new row

with_new_row = np.vstack((original, new_row))
print(original)
print("Array with new row:", with_new_row)  

# Adding a new column
new_column = np.array([[7], [8]])
with_new_column = np.hstack((original, new_column))
print("Array with new column:", with_new_column)    

# Removing elements
arr = np.array([1, 2, 3, 4, 5])
# Remove the element at index 2
removed_element = np.delete(arr, 2)
print("Array after removing element at index 2:", removed_element)