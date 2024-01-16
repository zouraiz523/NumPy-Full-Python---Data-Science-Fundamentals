import numpy as np  

# Creating a NumPy array
a = np.array([1, 2, 3, 4, 5])

# Printing the NumPy array
print(a)  # Output: [1 2 3 4 5]

# Printing the type of the variable (NumPy array)
print(type(a))  # Output: <class 'numpy.ndarray'>

# Example 2

# Creating a NumPy array
a = np.array([1, 2, 3, 4, 5])

# Printing the NumPy array
print(a)  # Output: [1 2 3 4 5]

# Accessing the element at index 1
print(a[1])  # Output: 2

# Slicing from index 1 to 1 (exclusive), resulting in an empty array
print(a[1:1])  # Output: []

# Slicing from the beginning to the 3rd-to-last element
print(a[:-2])  # Output: [1 2 3]

# Modifying the element at index 2 to be 10
a[2] = 10
print(a)  # Output: [1 2 10 4 5]


