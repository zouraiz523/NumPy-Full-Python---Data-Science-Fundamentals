# Exporting (Saving) NumPy Array

import numpy as np

# Creating a NumPy array
a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])

# Save the array to a file
np.save("myarray.npy", a)


# Importing (Loading) NumPy Array
# Load the array from the file
loaded_array = np.load("myarray.npy")

# Display the loaded array
print("Loaded Array:")
print(loaded_array)
