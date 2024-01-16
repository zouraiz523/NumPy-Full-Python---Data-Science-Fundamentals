import numpy as np
# Filling Arrays
# Example 1
a = np.full((10, 10, 10, 10), 9)
print(a)

# Example 2
a = np.zeros((10, 5, 2))
print(a)

# Example 3 (Corrected)
a = np.ones((10, 2))
print(a)

# Example 4
a = np.empty((5, 5, 5))
print(a)

# Example 5 (Corrected)
x_values = np.arange(0, 1005, 5)
print(x_values)

# Example 6 (Corrected)
x_values = np.linspace(0, 1000, 5)
print(x_values)
