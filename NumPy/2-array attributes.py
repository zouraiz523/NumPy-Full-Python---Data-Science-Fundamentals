
import numpy as np  

a_mul = np.array([[[[1, 2, 3, 1],
                    [4, 5, 6, 1],
                    [7, 8, 9, 1]],
                   [[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]]]])

# Printing the shape of the array
print(a_mul.shape)  # Output: (1, 2, 3, 4)

# Printing the number of dimensions
print(a_mul.ndim)   # Output: 4

# Printing the total number of elements in the array
print(a_mul.size)   # Output: 24

# Printing the data type of the array
print(a_mul.dtype)  # Output: int64
