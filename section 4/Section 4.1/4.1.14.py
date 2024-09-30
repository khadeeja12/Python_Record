import numpy as np

array_x = np.array([1, 2, 3, 4, 5])
array_y = np.array([5, 6, 2, 3, 8])

data = np.array([array_x, array_y])
covariance_matrix = np.cov(data)

print("Array X:")
print(array_x)
print("\nArray Y:")
print(array_y)
print("\nCovariance Matrix:")
print(covariance_matrix)
