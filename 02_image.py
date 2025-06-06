import numpy as np
import matplotlib.pyplot as plt


array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.random.rand(3,3)
array3 = np.zeros((4, 4))

#save arrays to file
np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)

#load arrays from file
loaded_array1 = np.load('array1.npy')
print(loaded_array1)

try:
    logo = np.load('numpy-logo.npy')

    # Display the logo
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title('Numpy Logo')
    plt.grid(False)

    dark_logo = 1- logo  # Invert the logo colors

    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title('Dark Numpy Logo')
    plt.grid(False)
    plt.show()
except FileNotFoundError:
    print("File not found. Please check the file path.")

