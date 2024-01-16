import numpy as np  

a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Printing the data types of the array elements
print(a_mul.dtype)

# Accessing the type of the element at the first row and first column
print(type(a_mul[0][0]))

# Example2
a_mul = np.array([[1, 2, 3],
                  [4, "hello", 6],
                  [7, 8, 9]])

# Printing the data types of the array elements
print(a_mul.dtype)

# Accessing the type of the element at the first row and first column
print(type(a_mul[0][0].dtype))

#Example 3

import numpy as np  

a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=np.int32)

# Printing the data types of the array elements
print(a_mul.dtype)

# Accessing the type of the element at the first row and first column
print(type(a_mul[0][0].dtype))


# Example 4

import numpy as np  

a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=np.float32)

# Printing the data types of the array elements
print(a_mul.dtype)

# Accessing the type of the element at the first row and first column
print(type(a_mul[0][0].dtype))

# Example 5

import numpy as np  

d = {'1': 'A'}

a_mul = np.array([[1, 2, 3],
                  [4, d, 6],
                  [7, 8, 9]], dtype=object)

print(a_mul.dtype)


#--------------------------------------

import numpy as np  

d = {'1': 'A'}

a_mul = np.array([[1, 2, 3],
                  [4, d, 6],
                  [7, 8, "hello"]])

# Printing the data types of the array elements
print(a_mul.dtype)

# Accessing the type of the element at the second row and first column
print(type(a_mul[1][0]))

# Example 6


import numpy as np  

d = {'1': 'A'}

a_mul = np.array([[1, 2, 3],
                  [4, d, 6],
                  [7, 8, "hello"]])

# Printing the data types of the array elements
print(a_mul.dtype)

# Accessing the type of the element at the second row and first column
print(type(a_mul[1][0]))


