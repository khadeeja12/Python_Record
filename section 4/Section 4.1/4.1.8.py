import numpy as np


complex_array = np.array([3 + 2j, 1 + 5j, 2 + 1j, 1 + 1j, 2 + 3j])

sorted_array = np.sort_complex(complex_array)

print("Original Complex Array:")
print(complex_array)
print("\nSorted Complex Array:")
print(sorted_array)
