import numpy as np

a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])

print("Original shape:", a.shape)
print("Reshaped to (5, 4):\n", a.reshape((5, 4)))
print("Reshaped to (20,):\n", a.reshape((20,)))
print("Reshaped to (20, 1):\n", a.reshape((20, 1)))
print("Reshaped to (20, 10) [Note: Total size mismatch]:\n", a.reshape((20, 10)))
print("Reshaped to (2, 2, 5):\n", a.reshape((2, 2, 5)))
print("Reshaped to (2, 5, 2):\n", a.reshape((2, 5, 2)))
print("Reshaped to (5, 2, 2):\n", a.reshape((5, 2, 2)))
