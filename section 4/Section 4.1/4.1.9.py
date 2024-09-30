import numpy as np

array = np.array([[3, 1, 2],
                  [6, 5, 4],
                  [1, 8, 7]])

n = 1
sorted_array = array[array[:, n].argsort()]

print("Original Array:")
print(array)
print(f"\nSorted Array by column {n}:")
print(sorted_array)
