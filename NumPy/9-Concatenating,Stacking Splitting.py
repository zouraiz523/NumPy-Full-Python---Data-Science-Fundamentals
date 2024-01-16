import numpy as np

a1 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]])
a2 = np.array([[11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])

# Appending elements to the NumPy array
a = np.concatenate((a1, a2), axis=1)
print(a)
