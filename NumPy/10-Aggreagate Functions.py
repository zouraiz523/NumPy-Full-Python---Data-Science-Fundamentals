import numpy as np

a1 = np.array([[1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24]])

# Corrected code
print(a1.min())
print(a1.max())
print(a1.mean())
print(a1.std())
print(a1.sum())
print(np.median(a1))
