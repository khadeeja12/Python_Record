import numpy as np

array_x = np.array([1, 2, 3, 4, 5])
array_y = np.array([5, 4, 3, 2, 1])

cross_correlation = np.correlate(array_x, array_y, mode='full')

print("Array X:")
print(array_x)
print("\nArray Y:")
print(array_y)
print("\nCross-Correlation:")
print(cross_correlation)
