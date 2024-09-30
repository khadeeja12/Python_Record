import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

mean = np.mean(array, axis=1)
std_dev = np.std(array, axis=1)
variance = np.var(array, axis=1)

print("Array:")
print(array)
print("\nMean along the second axis:")
print(mean)
print("\nStandard Deviation along the second axis:")
print(std_dev)
print("\nVariance along the second axis:")
print(variance)
