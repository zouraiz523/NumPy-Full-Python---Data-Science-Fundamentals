import numpy as np

a = np.array([1, 2, 3])

# Appending elements to the NumPy array
a = np.append(a, [7, 8, 9])

print(a)
import numpy as np

a = np.array([1, 2, 3])

# Appending elements to the NumPy array
a = np.append(a, [7, 8, 9])

# Inserting values into the NumPy array at specific indices
indices = [1, 3, 5]
values_to_insert = [10, 11, 12]
a = np.insert(a, indices, values_to_insert)

print(a)
