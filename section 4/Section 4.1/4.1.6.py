import numpy as np

array = np.array([[3, 1, 2],
                  [6, 5, 4]])

sorted_first_axis = np.sort(array, axis=0)
sorted_last_axis = np.sort(array, axis=1)
sorted_flattened = np.sort(array, axis=None)

print("Original Array:")
print(array)
print("\nSorted along the first axis:")
print(sorted_first_axis)
print("\nSorted along the last axis:")
print(sorted_last_axis)
print("\nSorted flattened array:")
print(sorted_flattened)
