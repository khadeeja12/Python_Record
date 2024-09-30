import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

percentile_80 = np.percentile(array, 80, axis=1)

print("Array:")
print(array)
print("\n80th Percentile along the second axis:")
print(percentile_80)
