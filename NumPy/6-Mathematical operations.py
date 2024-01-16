import numpy as np 

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

a1 = np.array(l1)
a2 = np.array(l2)

# Element-wise addition of the NumPy arrays
print(a1 + a2)

# Element-wise subtraction of the NumPy arrays
print(a1 - a2)

# Corrected array definition
a = np.array([[1, 2, 3],
              [4, 5, 5]])

# Square root of the array (assuming all elements are non-negative)
print(np.sqrt(a))
